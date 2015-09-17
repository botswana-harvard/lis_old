from lis.base.model.tests.factories import BaseLabUuidModelFactory

from lis.labeling.models import LabelPrinter


class LabelPrinterFactory(BaseLabUuidModelFactory):
    FACTORY_FOR = LabelPrinter

    cups_printer_name = 'CUPS'
    cups_server_ip = '127.0.0.1'
    default = True
