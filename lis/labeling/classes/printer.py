import cups

from ..exceptions import LabelPrinterError


class Printer(object):
    """A simple wrapper class for cups."""

    def __init__(self, printer_name=None, cups_server_host=None):
        self.conn = None
        self.printer = None
        self.printer_name = printer_name or 'default'
        cups.setServer(cups_server_host or 'localhost')
        self.server = cups.getServer()
        try:
            self.conn = cups.Connection()
        except RuntimeError:
            raise LabelPrinterError('Failed to connect to print server {0}'.format(cups.getServer()))
        try:
            if self.printer_name == 'default':
                self.printer = self.conn.getDests()[(None, None)]
                self.printer_name = self.printer.name
            else:
                self.printer = self.conn.getDests()[(self.printer_name, None)]
        except KeyError:
            raise LabelPrinterError('Failed to find a print \'{}\' on cups server \'{}\''.format(
                self.printer_name, cups.getServer()))

    def print_file(self, file_name, title="edc_label"):
        """Prints a file and returns a job_id using the cups connection
        without letting cups render the output (raw).

        Raises a LabelPrinterError if cups.Connection().printFile raises an error."""
        try:
            job_id = self.conn.printFile(self.printer.name, file_name, title, {'raw': file_name})
        except (cups.IPPError, RuntimeError) as ipp_error:
            raise LabelPrinterError(('Unable to print to \'{}\'  '
                                     '\'{}\'. Got \'{}\'').format(
                                         self.printer.name,
                                         self.server,
                                         str(ipp_error)))
        return job_id

    def __repr__(self):
        return 'Printer({0}, {1})'.format(self.printer.name, self.server)

    def __str__(self):
        return '{}@{}'.format(self.printer.name, self.server)
