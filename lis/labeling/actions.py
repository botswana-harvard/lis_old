from django.contrib import messages
from django.core.exceptions import ImproperlyConfigured

from .classes import Label, QuerysetLabel, AliquotLabel
from .exceptions import LabelPrinterError


def print_test_label(modeladmin, request, queryset):
    for zpl_template in queryset:
        label = Label(template=zpl_template)
        label.print_label()
    modeladmin.message_user(request, label.message)
print_test_label.short_description = "Print test label to default printer "


def print_aliquot_label(modeladmin, request, aliquots):
    """ Prints an aliquot label."""
    aliquot_label = AliquotLabel()
    try:
        for aliquot in aliquots:
            aliquot_label.print_label_for_aliquot(request, aliquot)
    except LabelPrinterError as label_printer_error:
        messages.add_message(request, messages.ERROR, str(label_printer_error))
print_aliquot_label.short_description = "LABEL: print aliquot label"
