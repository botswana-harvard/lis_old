from django.contrib import admin

from ..models import Protocol
from edc_base.modeladmin_mixins.model_admin_audit_fields_mixin import audit_fieldset_tuple


@admin.register(Protocol)
class ProtocolAdmin(admin.ModelAdmin):

    fieldsets = (
        (None, {
            'fields': [
                'name',
                'title',
            ]}), audit_fieldset_tuple)

    list_display = (
        'name', 'title', 'created')

    list_filter = ('created', )

    search_fields = ('name', 'title')
