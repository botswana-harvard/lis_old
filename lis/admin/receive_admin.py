from django.contrib import admin
from edc_base.modeladmin_mixins.model_admin_audit_fields_mixin import audit_fieldset_tuple

from ..models import Receive
from ..forms import ReceiveForm


@admin.register(Receive)
class ReceiveAdmin(admin.ModelAdmin):

    form = ReceiveForm

    fieldsets = (
        (None, {
            'fields': [
                'specimen_identifier',
                'receive_datetime',
                'patient',
                'protocol_number',
            ]}),
        ('Specimen', {
            'fields': [
                'collection_datetime',
                'specimen_type',
                'specimen_condition',
                'specimen_volume',
            ]}),
        ('Other', {
            'fields': [
                'clinician_initials',
                'other_reference',
            ]}),
        audit_fieldset_tuple)

#     radio_fields = {
#         'patient': admin.VERTICAL}

    list_display = (
        'receive_identifier',
        'specimen_identifier',
        'specimen_type',
        'patient',
        'protocol_number',
        'receive_datetime',
        'collection_datetime',
        'specimen_condition',
    )

    list_filter = (
        'receive_datetime',
        'collection_datetime',
        'specimen_condition',
        'specimen_type',
        'protocol_number',
        'created'
    )

    search_fields = (
        'receive_identifier',
        'specimen_identifier',
        'patient__subject_identifier'
    )
