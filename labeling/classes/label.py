import os
import subprocess
import tempfile
import threading

from datetime import datetime
from string import Template

from ..models import ZplTemplate, LabelPrinter


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
"""
    def __init__(self):
        self._zpl_template = None
        self._formatted_label = None
        self._label_printer = None
        self.zpl_template_string = None
        self.default_label_printer = None
        self.file_name = None
        self.client_addr = None
        self.label_context = {'barcode_value': '123456789'}
        self.message = None
        self.error_message = None
        self.process = None
        self.msgs = None

    @property
    def barcode_value(self):
        return self.label_context.get('barcode_value')

    @property
    def zpl_template(self):
        return self._zpl_template

    @zpl_template.setter
    def zpl_template(self, name_or_instance):
        """ Set zpl_template with a zpl_template name or an instance of ZplTemplate otherwise return None.

        Also sets the zpl_template_string using the ZplTemplate.template value."""
        self._zpl_template = None
        if isinstance(name_or_instance, ZplTemplate):
            self._zpl_template = name_or_instance
        elif isinstance(name_or_instance, basestring):
            self._zpl_template = ZplTemplate.objects.get(name=name_or_instance)
        else:
            raise TypeError('Unable to set the Zpl Template. Got {0}'.format(name_or_instance))
        self.zpl_template_string = self._zpl_template.template

    @property
    def formatted_label_string(self):
        """ Returns a label string formatted with zpl template string and the current label context. """
        return Template(self.zpl_template_string).safe_substitute(self.label_context)

    def print_label(self, copies, client_addr):
        """ Prints the label or throws an exception if the printer is not found. """
        print_success = False
        self.message = None
        self.error_message = None
        self.msgs = []
        self.client_addr = client_addr
        if not self.label_printer:
            self.error_message = 'Unable to determine the correct printer'
        else:
            # reverse order so labels are in order top to bottom on a strip
            for i in range(copies, 0, -1):
                self.label_context.update({
                    'label_count': i,
                    'label_count_total': copies,
                    'timestamp': datetime.today().strftime('%Y-%m-%d %H:%M')})
                if self.write_formatted_label_to_file():
                    # wrap the lpr process in a thread to allow for a timeout if printer not found.
                    # http://stackoverflow.com/questions/1191374/subprocess-with-timeout
                    timeout = 5
                    thread = threading.Thread(target=self.printing_processor)
                    thread.start()
                    thread.join(timeout)
                    if thread.is_alive():
                        self.process.terminate()
                        thread.join()
                    if self.process.returncode < 0:
                        # process timed out so throw an exception
                        self.error_message = ('Unable to connect to printer '
                                        '{0} ({1}){2}.'.format(unicode(self.label_printer),
                                                            self.process.returncode, self.client_addr))
                        #raise PrinterException(self.message)
                    elif self.error_message:
                        self.error_message = '{0} See printer {1}.'.format(self.error_message, self.label_printer.cups_printer_name)
                    else:
                        self.message = ('Successfully printed label \'{0}\' {1}/{2} to '
                                        '{3} from {4}'.format(self.barcode_value, (copies - i + 1), copies,
                                                     self.label_printer.cups_printer_name, self.client_addr))
                        print_success = True
        return (self.message, self.error_message, print_success)

    def printing_processor(self):
        """ Callback to run lpr in a thread. """
        self.process = subprocess.Popen(['lpr', '-P', self.label_printer.cups_printer_name, '-l',
                                        self.file_name, '-H', self.label_printer.cups_server_ip],
                                        shell=False,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE)
        self.message, self.error_message = self.process.communicate()

    def write_formatted_label_to_file(self):
        """ Write the formatted label to a text file for the printer """
        fd, self.file_name = tempfile.mkstemp()
        try:
            f = os.fdopen(fd, "w")
        except:
            self.message = ('Cannot print label. Unable to create/open temporary file {0}.'.format(self.file_name))
            return False
        f.write(self.formatted_label_string)
        f.close()
        return True

    @property
    def label_printer(self):
        """ Set the label printer by remote_addr or default"""
        if not self._label_printer:
            # get default for this client
            if LabelPrinter.objects.filter(client__ip=self.client_addr, default=True).count() == 1:
                self._label_printer = LabelPrinter.objects.get(client__ip=self.client_addr, default=True)
            # get for this client even if not default
            elif LabelPrinter.objects.filter(client__ip=self.client_addr, default=False).count() == 1:
                self._label_printer = LabelPrinter.objects.get(client__ip=self.client_addr, default=False)
            elif self.default_label_printer:
                self._label_printer = self.default_label_printer
            else:
                # last try, a local printer?
                if LabelPrinter.objects.filter(cups_server_ip='127.0.0.1').count() == 1:
                        self._label_printer = LabelPrinter.objects.get(cups_server_ip='127.0.0.1')
        return self._label_printer
