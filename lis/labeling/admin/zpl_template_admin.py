from django.contrib import admin

from ..actions import print_test_label
from ..forms import ZplTemplateForm
from ..models import ZplTemplate


class ZplTemplateAdmin(admin.ModelAdmin):

    form = ZplTemplateForm

    fields = (
        "name",
        "template",
        "default",
    )

    list_display = ('name', 'default',)
    radio_fields = {}
    filter_horizontal = ()
    actions = [print_test_label]

admin.site.register(ZplTemplate, ZplTemplateAdmin)
