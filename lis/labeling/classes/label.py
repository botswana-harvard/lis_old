import cups
import tempfile
import socket

from collections import namedtuple
from datetime import datetime
from string import Template

from django.conf import settings
from django.core.exceptions import MultipleObjectsReturned

from ..exceptions import LabelPrinterError
from ..models import ZplTemplate, LabelPrinter, Client

from .named_tuples import ClientTuple


class Label(object):
    """ Prints a label based on a template and it's context.

    An example of a ZPL template string is ::
        template_string = ('^XA\n'
            '^FO325,5^A0N,15,20^FD${label_count}/${label_count_total}^FS\n'
            '^FO320,20^BY1,3.0^BCN,50,N,N,N\n'
            '^BY^FD${barcode_value}^FS\n'
            '^FO320,80^A0N,15,20^FD${barcode_value}^FS\n'
            '^FO325,152^A0N,20^FD${timestamp}^FS\n'
            '^XZ')

    To change the timeout on 'lpr' from the default of 5 (seconds), use
    the settings attribute LABEL_PRINTER_TIMEOUT, e.g.
    LABEL_PRINTER_TIMEOUT = 25
"""
    def __init__(self):
        self._client = None
        self._cups_printer_name = None
        self._cups_server = None
        self._formatted_label = None
        self._label_printer = None
        self._zpl_template = None
        _, self.file_name = tempfile.mkstemp()
        self.debug = False
        self.label_context = {}
        self.message = None
        self.msgs = None
        self._conn = None
 
    @property
    def cups_printer_name(self):
        """Returns the cups printer name as queried from lab_printer.

        Strips of whitespace characters."""
        return self.label_printer.cups_printer_name.strip()

    @property
    def client(self):
        return self._client

    @client.setter
    def client(self, hostname_or_ip):
        """Sets the Client tuple of ip, hostname, etc and the label_printer if possible.

        .. note:: Request object accessed in the parent class returns
        the IP Address to help set this value, but here we always
        confirm that the hostname can be determined so make sure DNS
        or the host file is configured."""
        hostname, aliases, ip = self.resolve(hostname_or_ip)
        try:
            client = Client.objects.get(name=hostname)
            printer_name = client.label_printer.cups_printer_name
            self.cups_server = client.label_printer.cups_server_hostname
            cups_hostname = self.cups_server.hostname
            self._label_printer = client.label_printer
        except Client.DoesNotExist:
            self.cups_server = 'localhost'  # default
            cups_hostname = self.cups_server.hostname
            self._client = ClientTuple(hostname, aliases, ip, None, cups_hostname)
            try:
                printer_name = self.label_printer.cups_printer_name
            except AttributeError:
                printer_name = None
        self._client = ClientTuple(hostname, aliases, ip, printer_name, cups_hostname)

    @property
    def cups_server(self):
        return self._cups_server

    @cups_server.setter
    def cups_server(self, hostname_or_ip=None):
        CupsTuple = namedtuple('CupsTuple', 'hostname aliases ip')
        hostname_or_ip = hostname_or_ip or self.label_printer.cups_server_hostname or self.label_printer.cups_server_ip
        self._cups_server = CupsTuple(*self.resolve(hostname_or_ip))

    def resolve(self, hostname_or_ip):
        hostname, aliases, ip = None, None, None
        try:
            if hostname_or_ip == 'localhost':
                # don't want ip6
                hostname, aliases, ip = 'localhost', [], ['127.0.0.1']
            else:
                hostname, aliases, ip = socket.gethostbyaddr(hostname_or_ip)
        except (socket.gaierror, socket.herror):
            try:
                ip = socket.gethostbyname(hostname_or_ip)
                hostname, aliases, ip = socket.gethostbyaddr(ip)
            except (socket.gaierror, socket.herror):
                raise TypeError('Expected a valid hostname. Update the hosts file or DNS. Got {}'.format(hostname_or_ip))
        return hostname, aliases, ip

    @property
    def zpl_template(self):
        return self._zpl_template

    @zpl_template.setter
    def zpl_template(self, name_or_instance):
        """ Set zpl_template with a zpl_template name or an instance of
        ZplTemplate otherwise return None."""
        self._zpl_template = None
        try:
            self._zpl_template = ZplTemplate.objects.get(name=name_or_instance)
        except ZplTemplate.DoesNotExist:
            self._zpl_template = name_or_instance

    @property
    def cups_connection(self):
        if not self._conn:
            self._conn = cups.Connection(self.cups_server.ip[0])
        return self._conn

    @property
    def formatted_label_string(self):
        """ Returns a label string formatted with zpl template string and the current label context. """
        return Template(self.zpl_template.template).safe_substitute(self.label_context)

    def print_label(self, copies=None, client_addr=None, debug=None, label_printer=None):
        """ Prints the label or throws an exception if the printer is not found. """
        self.debug = debug or False
        self.message = None
        self.msgs = []
        copies = copies or 1
        self.client = client_addr or 'localhost'
        if label_printer:
            self._label_printer = label_printer
        if self.label_printer:
            # reverse order so labels are in order top to bottom on a strip
            for i in range(copies, 0, -1):
                self.label_context.update({
                    'label_count': i,
                    'label_count_total': copies,
                    'timestamp': datetime.today().strftime('%Y-%m-%d %H:%M')})
                if self.debug:
                    print ('client_addr \'{}\''.format(client_addr))
                    print ('template \'{}\''.format(self.zpl_template))
                    print ('label_printer \'{}\', default=\'{}\''.format(self.label_printer, self.label_printer.default))
                    print ('cups printer name \'{}\''.format(self.label_printer.cups_printer_name))
                    print ('cups_server_ip \'{}\''.format(self.cups_server.ip))
                    print ('cups_server_name \'{}\''.format(self.cups_server.hostname))
                with open(self.file_name, 'w') as f:
                    f.write(self.formatted_label_string)
                try:
                    job_id = self.cups_connection.printFile(self.cups_printer_name,
                                                            self.file_name,
                                                            "edc_label",
                                                            {'raw': self.file_name}  # don't let CUPS render!
                                                            )
                    self.message = ('Successfully printed {1}/{2} label(s) \'{0}\' to '
                                    '{3} (default={4}) on CUPS@{5} for client \'{7}\' Job_ID {6}'.format(
                                        self.label_context.get('barcode_value'),
                                        (copies - i + 1),
                                        copies,
                                        self.cups_printer_name,
                                        self.label_printer.default,
                                        self.cups_server.hostname,
                                        job_id,
                                        self.client.hostname))
                except (cups.IPPError, RuntimeError) as ipp_error:
                    raise LabelPrinterError(('Unable to print to \'{}\' on CUPS server @ '
                                             '\'{}\'. Got \'{}\'').format(
                                                 self.cups_printer_name,
                                                 self.cups_server.hostname,
                                                 str(ipp_error)))
        return self.message

    @property
    def label_printer(self):
        """ Sets the label printer specified for the client otherwise the default.

        Uses settings attribute list LABEL_PRINTER_MAKE_AND_MODEL from CUPS.
        For example::
            LABEL_PRINTER_MAKE_AND_MODEL = ['Zebra ZPL Label Printer']."""
        if not self._label_printer:
            if self.debug:
                print ('LabelPrinter not set by Client. Searching CUPS and EDC LabelPrinter')
            # try for a label printer in CUPS set to default in CUPS
            dest = self.cups_connection.getDests().get((None, None))
            if dest:
                if dest.options['printer-make-and-model'] in settings.LABEL_PRINTER_MAKE_AND_MODEL:
                    try:
                        if self.debug:
                            print ('Default in CUPS is {}@{}'.format(dest.name, self.cups_server.hostname))
                        self._label_printer = LabelPrinter.objects.get(
                            cups_printer_name=dest.name,
                            cups_server_hostname=self.cups_server.hostname,
                            )
                        if self.debug:
                            print ('Selected EDC LabelPrinter {}@{} that is the default in CUPS.'.format(dest.name, self.cups_server.hostname))
                    except LabelPrinter.DoesNotExist:
                        if self.debug:
                            print ('... not selecting {}@{}. Not an EDC LabelPrinter'.format(dest.name, self.cups_server.hostname))
                        pass
            if not self._label_printer:
                # try for a label printers in CUPS set to default in the EDC?
                if self.debug:
                    print ('Searching for any CUPS printer that is the default EDC LabelPrinter.')
                cups_printer_names = []
                for dest in self.cups_connection.getDests().itervalues():
                    if dest.options['printer-make-and-model'] in settings.LABEL_PRINTER_MAKE_AND_MODEL:
                        try:
                            cups_printer_names.append(dest.name)
                            self._label_printer = LabelPrinter.objects.get(
                                cups_printer_name=dest.name,
                                cups_server_hostname=self.cups_server.hostname,
                                default=True)
                            if self.debug:
                                print ('Selected CUPS {}@{} that is default LabelPrinter in EDC.'.format(dest.name, self.cups_server.hostname))
                            break
                        except LabelPrinter.DoesNotExist:
                            if self.debug:
                                print ('... not selecting CUPS {}@{}. Not the default EDC LabelPrinter or not found'.format(dest.name, self.cups_server.hostname))
                            pass
            if not self._label_printer:
                try:
                    self._label_printer = LabelPrinter.objects.get(cups_printer_name__in=cups_printer_names,
                                                                   default=False)
                    if self.debug:
                        print ('Selected the default in LabelPrinter, {}'.format(dest.name, self.cups_server.hostname))
                except MultipleObjectsReturned:
                    self._label_printer = None
                    raise LabelPrinterError('Unable to select a label printer for client \'{0}\'.\nClient not '
                                            'listed in EDC and more than one CUPS label printer is available in '
                                            'model LabelPrinter (default=False). '
                                            '\nTry any of the following:\n1. add the default '
                                            'CUPS printer to model LabelPrinter\n2. set any CUPS label printer '
                                            'as the default label printer in model LabelPrinter'
                                            '\n3. add client \'{0}\' to model Client and associate '
                                            'with a printer in model LabelPrinter.'.format(self.client.hostname))
                except LabelPrinter.DoesNotExist:
                    self._label_printer = None
                    raise LabelPrinterError('Unable to select a label printer for client '
                                            '\'{0}\'.\nTry any of the following:\n1. add the default '
                                            'CUPS printer to model LabelPrinter\n2. set any CUPS label printer '
                                            'as the default label printer in model LabelPrinter'
                                            '\n3. add client \'{0}\' to model Client and associate '
                                            'with a printer in model LabelPrinter.'.format(self.client.hostname))
        return self._label_printer
