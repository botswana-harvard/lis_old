import tempfile

from datetime import datetime, date
from string import Template

from ..exceptions import LabelPrinterError


class Label(object):

    def __init__(self, printer, template=None, context=None):
        self.label_context = context or {}
        self.message = None
        self.template = template or ''
        self.printer = printer
        _, self.file_name = tempfile.mkstemp()

    def print_label(self, copies=None, debug=False):
        """ Prints the label combining the template and its context."""
        self.message = None
        self.msgs = []
        copies = copies or 1
        # reverse order so labels are in order top to bottom on a strip
        for i in range(copies, 0, -1):
            self.label_context.update({
                'label_count': i,
                'label_count_total': copies,
                'timestamp': datetime.today().strftime('%Y-%m-%d %H:%M')})
            if debug:
                self.print_debug()
            with open(self.file_name, 'w') as f:
                f.write(Template(self.template).safe_substitute(self.label_context))
            try:
                job_id = self.printer.print_file(self.file_name)
                self.message = ('Successfully printed {1}/{2} label(s) \'{0}\' to '
                                '{3} Job ID {4}'.format(
                                    self.label_context.get('barcode_value'),
                                    (copies - i + 1),
                                    copies,
                                    str(self.printer),
                                    job_id))
            except LabelPrinterError as msg:
                self.message = msg
                break
        return self.message

    def print_test_label(self, copies=None, debug=False):
        """Prints a test label using a ZPL tepmplate.

        For example::
            from lis.labeling.classes import Label
            label = Label(printer_name='Zebra_Technologies_ZTC_GK420t_2')
            label.print_test_label()
        """
        self.template = ('^XA\n'
                         '^FO310,15^A0N,20,20^FD${protocol} Site ${site} ${clinician_initials}   ${aliquot_type} ${aliquot_count}${primary}^FS\n'
                         '^FO310,34^BY1,3.0^BCN,50,N,N,N\n'
                         '^BY^FD${aliquot_identifier}^FS\n'
                         '^FO310,92^A0N,20,20^FD${aliquot_identifier}^FS\n'
                         '^FO310,112^A0N,20,20^FD${subject_identifier} (${initials})^FS\n'
                         '^FO310,132^A0N,20,20^FDDOB: ${dob} ${gender}^FS\n'
                         '^FO310,152^A0N,25,20^FD${drawn_datetime}^FS\n'
                         '^XZ')
        self.label_context = {'barcode_value': '12345',
                              'protocol': 'BHPXXX',
                              'site': '00',
                              'clinician_initials': 'CC',
                              'aliquot_type': 'WB',
                              'aliquot_count': '1',
                              'primary': '<',
                              'aliquot_identifier': 'AAXXXXX',
                              'subject_identifier': '000-123456789',
                              'initials': 'AA',
                              'dob': date.today(),
                              'gender': 'F',
                              'drawn_datetime': format(datetime.today(), '%Y-%m-%d %H:%m')}
        return self.print_label(copies, debug)

    def print_debug(self):
        print 'template \'{}\''.format(self.zpl_template)
        print 'label_printer \'{}\', default=\'{}\''.format(self.label_printer, self.label_printer.default)
        print 'printer name \'{}\''.format(self.printer.name)
        print 'is_default \'{}\''.format(self.printer.is_default)
        print 'cups_server \'{}\''.format(self.printer.server)
