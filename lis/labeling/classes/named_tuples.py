from collections import namedtuple

LabelPrinterTuple = namedtuple('LabelPrinterTuple', 'cups_printer_name cups_server_hostname cups_server_ip default')
ClientTuple = namedtuple('ClientTuple', 'hostname aliases ip printer_name cups_hostname')
ZplTemplateTuple = namedtuple('ZplTemplateTuple', 'name template default')
