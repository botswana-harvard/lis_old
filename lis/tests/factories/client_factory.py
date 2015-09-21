import factory

from lis.base.model.tests.factories import BaseLabUuidModelFactory

from lis.labeling.models import Client

from .label_printer_factory import LabelPrinterFactory


class ClientFactory(BaseLabUuidModelFactory):
    FACTORY_FOR = Client

    ip = '127.0.0.1'
    name = 'Client'
    label_printer = factory.SubFactory(LabelPrinterFactory)
