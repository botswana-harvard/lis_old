import cups
import tempfile
import socket

from collections import namedtuple
from datetime import datetime
from string import Template

from django.core.exceptions import MultipleObjectsReturned

from ..models import ZplTemplate, LabelPrinter

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
        self._cups_printer_name = None
        self._cups_server = None
        self._formatted_label = None
        self._label_printer = None
        self._zpl_template = None
        _, self.file_name = tempfile.mkstemp()
        self.error_message = None
        self.label_context = {}
        self.message = None
        self.msgs = None
 
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
        """Sets the Client tuple of ip, hostname, etc.

        .. note:: Request object accessed in the parent class returns
        the IP Address to help set this value, but here we always
        confirm that the hostname can be determined so make sure DNS
        or the host file is configured."""
        hostname, aliases, ip = self.resolve(hostname_or_ip)
        self._client = ClientTuple(hostname, aliases, ip, None, None)

    @property
    def cups_server(self):
        if not self._cups_server:
            CupsTuple = namedtuple('CupsTuple', 'hostname aliases ip')
            hostname_or_ip = self.label_printer.cups_server_hostname or self.label_printer.cups_server_ip
            self._cups_server = CupsTuple(*self.resolve(hostname_or_ip))
        return self._cups_server

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
    def formatted_label_string(self):
        """ Returns a label string formatted with zpl template string and the current label context. """
        return Template(self.zpl_template.template).safe_substitute(self.label_context)

    def print_label(self, copies=None, client_addr=None, debug=False):
        """ Prints the label or throws an exception if the printer is not found. """
        print_success = False
        self.message = None
        self.error_message = None
        self.msgs = []
        copies = copies or 1
        self.client = client_addr or 'localhost'
        if self.label_printer:
            # reverse order so labels are in order top to bottom on a strip
            for i in range(copies, 0, -1):
                self.label_context.update({
                    'label_count': i,
                    'label_count_total': copies,
                    'timestamp': datetime.today().strftime('%Y-%m-%d %H:%M')})
                if debug:
                    print 'client_addr \'{}\''.format(client_addr)
                    print 'template \'{}\''.format(self.zpl_template)
                    print 'label_printer \'{}\', default=\'{}\''.format(self.label_printer, self.label_printer.default)
                    print 'cups printer name \'{}\''.format(self.label_printer.cups_printer_name)
                    print 'cups_server_ip \'{}\''.format(self.cups_server.ip)
                    print 'cups_server_name \'{}\''.format(self.cups_server.hostname)
                with open(self.file_name, 'w') as f:
                    f.write(self.formatted_label_string)
                try:
                    conn = cups.Connection(self.cups_server.ip[0])
                    job_id = conn.printFile(self.cups_printer_name,
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
                    print_success = True
                except (cups.IPPError, RuntimeError) as ipp_error:
                    self.error_message = ('Unable to print to \'{}\' on CUPS server @ '
                                          '\'{}\'. Got \'{}\'').format(
                                              self.cups_printer_name,
                                              self.cups_server.hostname,
                                              str(ipp_error))
                    print_success = False
                    break
        return (self.message, self.error_message, print_success)

    @property
    def label_printer(self):
        """ Returns the label printer specified for the client otherwise the default."""
        if not self._label_printer:
            try:
                self._label_printer = LabelPrinter.objects.get(client__name=self.client.hostname)
            except LabelPrinter.DoesNotExist:
                try:
                    # client has not entry, just use default printer
                    self._label_printer = LabelPrinter.objects.get(default=True)
                except MultipleObjectsReturned:
                    self._label_printer = None
                    self.error_message = ('Unable to select a printer for client \'{}\'. Client not '
                                          'listed and more than one label printer is set as default.'
                                          ).format(self.client.hostname)
                except LabelPrinter.DoesNotExist:
                    self._label_printer = None
                    self.error_message = ('Unable to select a printer for client '
                                          '\'{}\'.').format(self.client.hostname)
        return self._label_printer
