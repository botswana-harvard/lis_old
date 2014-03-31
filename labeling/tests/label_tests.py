import os.path

from django.test import TestCase

from ..classes import Label

from .factories import LabelPrinterFactory, ClientFactory, ZplTemplateFactory


class LabelTests(TestCase):

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
^FO320,110^A0N,15,20^FD${barcode_value}^FS
^FO325,130^A0N,15,20^FDCD4^FS
^FO325,150^A0N,20^FD${created}^FS
^XZ""")

        self.zpl_template = ZplTemplateFactory(
                name='Default template',
                default=True,
                template=self.default_zpl_template_string)

    def test_barcode_value(self):
        label = Label()
        label.zpl_template = self.zpl_template
        self.assertEqual(label.barcode_value, '123456789')

    def test_formatted_label(self):
        """Assert formatted label contains the barcode value."""
        label = Label()
        label.zpl_template = self.zpl_template
        self.assertIsNotNone(label.formatted_label_string)
        self.assertTrue(label.barcode_value in label.formatted_label_string)

    def test_label_context(self):
        label = Label()
        label.zpl_template_string = self.default_zpl_template_string
        self.assertTrue('barcode_value' in label.label_context)

    def test_write_print_file(self):
        """Assert can write label to a temp file."""
        label = Label()
        label.zpl_template = self.zpl_template
        self.assertTrue(label.write_formatted_label_to_file())
        self.assertTrue(os.path.isfile(label.file_name))

    def test_template1(self):
        label = Label()
        label.zpl_template = self.zpl_template
        label.zpl_template_string = label.zpl_template.template
        self.assertIsNotNone(label.zpl_template_string)

    def test_template2(self):
        label = Label()
        label.zpl_template = self.zpl_template
        label.zpl_template_string = label.zpl_template.template
        self.assertIsNotNone(label.zpl_template_string)

    def test_label_printer1(self):
        """Assert can determine the label printer if have a default printer."""
        label = Label()
        label.zpl_template = self.zpl_template
        label.default_label_printer = self.label_printer_default
        self.assertIsNotNone(label.label_printer)
        self.assertEquals(label.label_printer.cups_server_ip, '127.0.0.1')

    def test_label_printer2(self):
        """Assert for a given client address, can determine the label printer if there is a default"""
        label = Label()
        label.zpl_template = self.zpl_template
        label.client_addr = '127.0.0.2'
        label.default_label_printer = self.label_printer_default
        self.assertTrue(label.label_printer, self.label_printer_default)
        self.assertFalse('Unable to determine the label printer for client {0}'.format(label.client_addr) in label.message)

    def test_label_printer3(self):
        """Assert for a given client address, cannot determine the label printer if there isn't a default."""
        self.label_printer_default.default = False
        self.label_printer_default.cups_server_ip = '127.0.0.127'
        self.label_printer_default.save()
        self.label_printer_client_10.default = False
        self.label_printer_client_10.save()
        self.label_printer_client_11_default.default = False
        self.label_printer_client_11_default.save()
        label = Label()
        label.zpl_template = self.zpl_template
        label.client_addr = '127.0.0.2'
        label.default_label_printer = None
        self.assertIsNone(label.label_printer)

    def test_label_printer3a(self):
        """Assert for a given client address, picks localhost label printer if there isn't a default."""
        self.label_printer_default.default = False
        self.label_printer_default.save()
        self.label_printer_client_10.default = False
        self.label_printer_client_10.save()
        self.label_printer_client_11_default.default = False
        self.label_printer_client_11_default.save()
        label = Label()
        label.zpl_template = self.zpl_template
        label.client_addr = '127.0.0.2'
        label.default_label_printer = None
        self.assertEquals(label.label_printer, self.label_printer_default)

    def test_label_printer3b(self):
        """Assert for a given client address, does not picks localhost label printer if there is a default."""
        self.label_printer_default.default = False
        self.label_printer_default.save()
        self.label_printer_client_10.default = False
        self.label_printer_client_10.save()
        self.label_printer_client_11_default.default = False
        self.label_printer_client_11_default.save()
        label = Label()
        label.zpl_template = self.zpl_template
        label.client_addr = '127.0.0.2'
        label.default_label_printer = self.label_printer_client_11
        self.assertEquals(label.label_printer, self.label_printer_client_11)

    def test_label_printer4a(self):
        """Assert for a given client address, can determine the label printer for the client."""
        label = Label()
        label.zpl_template = self.zpl_template
        label.client_addr = '127.0.0.10'
        label.default_label_printer = self.label_printer_default
        self.assertTrue(label.label_printer == self.label_printer_client_10)

    def test_label_printer4b(self):
        """Assert for a given client address, picks the overall default label printer if there is no printer defined for the client."""
        label = Label()
        label.zpl_template = self.zpl_template
        label.client_addr = '127.0.0.13'
        label.default_label_printer = self.label_printer_default
        self.assertEqual(label.label_printer, self.label_printer_default)

    def test_label_printer4c(self):
        """Assert for a given client address, picks the default (of 2 printers) for the client event though there is a general overall default printer."""
        label = Label()
        label.zpl_template = self.zpl_template
        label.client_addr = '127.0.0.11'
        label.default_label_printer = self.label_printer_default
        self.assertTrue(label.label_printer == self.label_printer_client_11_default)

    def test_label_printer5(self):
        """Assert for a given client address, can determine the assigned label printer."""
        label = Label()
        label.zpl_template = self.zpl_template
        label.client_addr = '127.0.0.10'
        label.default_label_printer = self.label_printer_default
        self.assertTrue(label.label_printer == self.label_printer_client_10)
