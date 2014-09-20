from django.core.management.base import BaseCommand

from ...classes import AliquotLabel
from lis.labeling.exceptions import LabelPrinterError


class Command(BaseCommand):
    help = 'Generate new encryption keys.'

    def handle(self, *args, **options):
        aliquot_label = AliquotLabel()
        print 'Print test label on CUPS server localhost'
        try:
            print aliquot_label.test('localhost')
        except LabelPrinterError as label_printer_error:
            print str(label_printer_error)
        print 'Done.'
