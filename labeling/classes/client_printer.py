import socket

from ..exceptions import LabelPrinterError
from ..models import Client, LabelPrinter

from .printer import Printer


class ClientPrinter(Printer):
    """Sets up the printer by selecting an instance of the
    Client model for a given IP address.

    Args:
      * client_addr: ip_address or hostname. client_addr will usually be
          passed from the REQUEST object. (Default: localhost).
          For example::
            client_addr = client_addr or request.META.get('REMOTE_ADDR')"""

    def __init__(self, client_addr, printer_name=None, cups_server_host=None):
        self.client = None
        self.is_default_printer = False
        ip_address = socket.gethostbyname(client_addr)
        try:
            self.client = Client.objects.get(ip=ip_address)
            printer_name = self.client.label_printer.cups_printer_name
            cups_server_host = self.client.label_printer.cups_server_hostname
            self.is_default_printer = self.client.label_printer.default
        except Client.DoesNotExist:
            try:
                label_printer = LabelPrinter.objects.get(default=True)
                printer_name = label_printer.cups_printer_name
                cups_server_host = label_printer.cups_server_hostname
                self.is_default_printer = True
            except LabelPrinter.DoesNotExist:
                raise LabelPrinterError('Failed to select a printer. Client {} is not associated '
                                        'with a Label Printer and no Label Printer has been set '
                                        'as the default.'.format(ip_address))
        super(ClientPrinter, self).__init__(printer_name, cups_server_host)
