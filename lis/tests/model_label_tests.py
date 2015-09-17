from django.test import TestCase
from django.db import models

from edc_base.model.models import BaseUuidModel

from lis.labeling.classes import ModelLabel
from lis.labeling.models import LabelPrinter

from .factories import LabelPrinterFactory, ClientFactory, ZplTemplateFactory

import factory


class TestModel(BaseUuidModel):

    f1 = models.CharField(max_length=10)
    f2 = models.CharField(max_length=10)
    f3 = models.CharField(max_length=10, null=True, blank=False)
    f4 = models.CharField(max_length=10, null=True, blank=False)
    f5 = models.CharField(max_length=10)

    def barcode_value(self):
        return self.f1

    class Meta:
        app_label = 'labeling'


class TestModelFactory(BaseUuidModel):
    FACTORY_FOR = TestModel

    f1 = factory.Sequence(lambda n: 'F1{0}'.format(n))
    f2 = factory.Sequence(lambda n: 'F2{0}'.format(n))
    f3 = factory.Sequence(lambda n: 'F3{0}'.format(n))
    f4 = factory.Sequence(lambda n: 'F4{0}'.format(n))
    f5 = factory.Sequence(lambda n: 'F5{0}'.format(n))


class ModelLabelTests(TestCase):

    def setUp(self):
        self.label_printer_default = LabelPrinterFactory(cups_server_ip='127.0.0.1', default=True)
        self.label_printer_client_10 = LabelPrinterFactory(cups_server_ip='127.0.0.3', default=True)
        self.label_printer_client_11_default = LabelPrinterFactory(cups_server_ip='127.0.0.4', default=True)
        self.label_printer_client_11 = LabelPrinterFactory(cups_server_ip='127.0.0.5', default=False)
        ClientFactory(ip='127.0.0.10', name='', label_printer=self.label_printer_client_10)
        ClientFactory(ip='127.0.0.11', name='', label_printer=self.label_printer_client_11)
        ClientFactory(ip='127.0.0.11', name='', label_printer=self.label_printer_client_11_default)
        self.default_zpl_template_string = ("""^XA
^FO325,15^A0N,15,20^FDBHHRL^FS
^FO310,30^BY2,3^BCN,75,N,N,N\n
^BY^FD${barcode_value}^FS
^FO320,110^A0N,15,20^FD${f1}^FS
^FO320,110^A0N,15,20^FD${f2}^FS
^FO320,110^A0N,15,20^FD${f3}^FS
^FO320,110^A0N,15,20^FD${f4}^FS
^FO325,130^A0N,15,20^FDCD4^FS
^FO325,150^A0N,20^FD${created}^FS
^XZ""")

        self.zpl_template = ZplTemplateFactory(
            name='Default template',
            default=True,
            template=self.default_zpl_template_string)

    def test_zpl_template_not_set(self):
        """Assert fails if template not set."""
        label = ModelLabel()
        test_model = TestModelFactory()
        request = None
        self.assertRaises(TypeError, label.print_label, request, test_model, update_messages=False, client_addr='127.0.0.1')

    def test_zpl_template(self):
        """Assert fails if template not set."""
        label = ModelLabel()
        TestModelFactory()
        label.zpl_template = self.zpl_template

    def test_print_label(self):
        """Assert sends error message if printer is not known to lpr."""
        test_model = TestModelFactory()
        label = ModelLabel()
        label.zpl_template = self.zpl_template
        label.default_label_printer = self.label_printer_default
        request = None
        label.print_label(request, test_model, update_messages=False, client_addr='127.0.0.1')
        self.assertIn('printer or class does not exist', label.error_message)

    def test_label_printer(self):
        """Assert fails if template not set."""
        label = ModelLabel()
        label.zpl_template = self.zpl_template
        self.assertIsNotNone(label.label_printer)
        self.assertTrue(isinstance(label.label_printer, LabelPrinter))

    def test_label_printer1(self):
        """Assert fails if template not set."""
        label = ModelLabel()
        TestModelFactory()
        label.zpl_template = self.zpl_template

    def test_label_context(self):
        """Assert can refresh the label context with the model instance."""
        label = ModelLabel()
        label.zpl_template = self.zpl_template
        test_model = TestModelFactory()
        label.model_instance = test_model
        self.assertTrue(label.refresh_label_context())

    def test_formatted_label_string(self):
        """Assert model values are in formatted label string."""
        label = ModelLabel()
        label.zpl_template = self.zpl_template
        test_model = TestModelFactory()
        label.model_instance = test_model
        label.refresh_label_context()
        self.assertIn(label.label_context.get('f1'), label.formatted_label_string)
        self.assertIn(label.label_context.get('f2'), label.formatted_label_string)
        self.assertIn(label.label_context.get('f3'), label.formatted_label_string)
        self.assertIn(label.label_context.get('f4'), label.formatted_label_string)
        self.assertIn(label.label_context.get('created'), label.formatted_label_string)
        self.assertIn(label.label_context.get('barcode_value'), label.formatted_label_string)
