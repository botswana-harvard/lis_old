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
    def __init__(self, client_addr=None):
        self.client_addr = client_addr or '127.0.0.1'
        self._zpl_template = None
        self._formatted_label = None
        self._label_printer = None
        self.default_label_printer = None
        _, self.file_name = tempfile.mkstemp()
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

    def print_label(self, copies=None, client_addr=None, test=False):
        """ Prints the label or throws an exception if the printer is not found. """
        print_success = False
        self.message = None
        self.error_message = None
        self.msgs = []
        copies = copies or 1
        self.client_addr = client_addr or self.client_addr
        if self.label_printer:
            # reverse order so labels are in order top to bottom on a strip
            for i in range(copies, 0, -1):
                self.label_context.update({
                    'label_count': i,
                    'label_count_total': copies,
                    'timestamp': datetime.today().strftime('%Y-%m-%d %H:%M')})
                if test:
                    print 'client_addr \'{}\''.format(client_addr)
                    print 'template \'{}\''.format(self.zpl_template)
                    print 'label_printer \'{}\', default=\'{}\''.format(self.label_printer, self.label_printer.default)
                    print 'Using default printer? {}'.format('Yes' if self.default_label_printer else 'No')
                    print 'cups printer name \'{}\''.format(self.label_printer.cups_printer_name)
                    print 'cups_server_ip \'{}\''.format(self.label_printer.cups_server_ip)
                with open(self.file_name, 'w') as f:
                    f.write(self.formatted_label_string)
                # wrap the lpr process in a thread to allow for a timeout if printer not found.
                # http://stackoverflow.com/questions/1191374/subprocess-with-timeout
                timeout = 10
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
                elif self.error_message:
                    self.error_message = '{0} See printer {1}.'.format(self.error_message,
                                                                       self.label_printer.cups_printer_name)
                else:
                    self.message = ('Successfully printed label \'{0}\' {1}/{2} to '
                                    '{3} from {4}'.format(self.barcode_value, (copies - i + 1), copies,
                                                          self.label_printer.cups_printer_name, self.client_addr))
                    print_success = True
        return (self.message, self.error_message, print_success)

    def printing_processor(self):
        """ Callback to run lpr in a thread. """
        self.process = subprocess.Popen(
            ['lpr', '-P', self.label_printer.cups_printer_name, '-l',
             self.file_name, '-H', self.label_printer.cups_server_ip],
            shell=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        self.message, self.error_message = self.process.communicate()

    @property
    def label_printer(self):
        """ Set the label printer by remote_addr or default"""
        self._label_printer = self.default_label_printer or None
        if not self._label_printer:
            try:
                # get for this client
                self._label_printer = LabelPrinter.objects.get(client__ip=self.client_addr)
            except LabelPrinter.DoesNotExist:
                try:
                    # get the default printer
                    self._label_printer = LabelPrinter.objects.get(default=True)
                    self.default_label_printer = self._label_printer 
                except LabelPrinter.DoesNotExist:
                    self._label_printer = None
                    self.error_message = 'Unable to select a printer for client \'{}\'.'.format(self.client_addr)
        return self._label_printer
