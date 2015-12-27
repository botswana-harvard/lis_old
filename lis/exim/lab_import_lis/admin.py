from django.contrib import admin

from edc_base.modeladmin.admin import BaseModelAdmin

from .actions import clear_stale_error_messages
from .models import LisImportError, LisLockModel, LisImportHistoryModel


class LisImportErrorAdmin(BaseModelAdmin):
    list_display = ('model_name', "identifier", 'created', "error_message")
    list_filter = ('model_name', 'created')
    search_fields = ("identifier", "error_message")
    actions = [clear_stale_error_messages]
admin.site.register(LisImportError, LisImportErrorAdmin)


class LisImportHistoryModelAdmin(BaseModelAdmin):
    list_display = ('lock_name', 'start_datetime', 'end_datetime')
    list_filter = ('start_datetime', 'end_datetime', 'lock_name', 'created')
admin.site.register(LisImportHistoryModel, LisImportHistoryModelAdmin)


class LisLockModelAdmin(BaseModelAdmin):
    list_filter = ('created', 'lock_name')
admin.site.register(LisLockModel, LisLockModelAdmin)
