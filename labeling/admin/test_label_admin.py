from django.contrib import admin
from django.contrib import messages

from ..actions import print_test_label
from ..classes import ModelLabel
from ..exceptions import PrinterException
from ..models import TestLabel


class TestLabelAdmin(admin.ModelAdmin):

    list_display = ('identifier', 'user_created', 'created')
    actions = [print_test_label, ]
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        model_label = ModelLabel()
        try:
            model_label.print_label(request, obj, obj.copies, obj.identifier)
        except PrinterException as e:
            messages.add_message(request, messages.ERROR, e.value)
        super(TestLabelAdmin, self).save_model(request, obj, form, change)

admin.site.register(TestLabel, TestLabelAdmin)
