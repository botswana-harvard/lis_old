from django.test import TestCase

from ..classes import Label

from .factories import LabelPrinterFactory, ClientFactory


class BarcodeTests(TestCase):

    def setUp(self):
        self.label_printer_default = LabelPrinterFactory(cups_server_ip='127.0.0.1', default=True)
        self.label_printer_client_10 = LabelPrinterFactory(cups_server_ip='127.0.0.3', default=True)
        self.label_printer_client_11_default = LabelPrinterFactory(cups_server_ip='127.0.0.4', default=True)
        self.label_printer_client_11 = LabelPrinterFactory(cups_server_ip='127.0.0.5', default=False)
        ClientFactory(ip='127.0.0.10', name='', label_printer=self.label_printer_client_10)
        ClientFactory(ip='127.0.0.11', name='', label_printer=self.label_printer_client_11)
        ClientFactory(ip='127.0.0.11', name='', label_printer=self.label_printer_client_11_default)

    def test_barcode_value(self):
        label = Label()
        label.zpl_template = label.default_template
        self.assertEqual(label.barcode_value, '123456789')

    def test_formatted_label(self):
        """Assert formatted label contains the barcode value."""
        label = Label()
        label.zpl_template = label.default_template
        self.assertTrue(label.barcode_value in label.formatted_label)

    def test_write_print_file(self):
        """Assert can write label to a temp file."""
        label = Label()
        label.zpl_template = label.default_template
        self.assertTrue(label.write_formatted_label_to_file())

    def test_label_printer1(self):
        """Assert can determine the label printer if have a default printer."""
        label = Label()
        label.zpl_template = label.default_template
        self.assertIsNotNone(label.label_printer)
        self.assertEquals(label.label_printer.cups_server_ip, '127.0.0.1')

    def test_label_printer2(self):
        """Assert for a given client address, can determine the label printer if there is a default"""
        label = Label()
        label.zpl_template = label.default_template
        label.client_addr = '127.0.0.2'
        self.assertTrue(label.label_printer, self.label_printer_default)
        self.assertFalse('Unable to determine the label printer for client {0}'.format(label.client_addr) in label.message)

    def test_label_printer3(self):
        """Assert for a given client address, cannot determine the label printer if there isn't a default."""
        self.label_printer_default.default = False
        self.label_printer_default.save()
        self.label_printer_client_11_default.default = False
        self.label_printer_client_11_default.save()
        label = Label()
        label.zpl_template = label.default_template
        label.client_addr = '127.0.0.2'
        self.assertIsNone(label.label_printer)
        self.assertTrue('Unable to determine the label printer for client {0}'.format(label.client_addr) in label.message)

    def test_label_printer4a(self):
        """Assert for a given client address, can determine the label printer for the client."""
        label = Label()
        label.zpl_template = label.default_template
        label.client_addr = '127.0.0.10'
        self.assertTrue(label.label_printer == self.label_printer_client_10)

    def test_label_printer4b(self):
        """Assert for a given client address, picks the overall default label printer if there is no printer defined for the client."""
        label = Label()
        label.zpl_template = label.default_template
        label.client_addr = '127.0.0.13'
        self.assertEqual(label.label_printer, self.label_printer_default)

    def test_label_printer4c(self):
        """Assert for a given client address, picks the default (of 2 printers) for the client event though there is a general overall default printer."""
        label = Label()
        label.zpl_template = label.default_template
        label.client_addr = '127.0.0.11'
        self.assertTrue(label.label_printer == self.label_printer_client_11_default)

    def test_label_printer5(self):
        """Assert for a given client address, can determine the assigned label printer."""
        label = Label()
        label.zpl_template = label.default_template
        label.client_addr = '127.0.0.10'
        self.assertTrue(label.label_printer == self.label_printer_client_10)
