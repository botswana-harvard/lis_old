from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..forms import PatientForm
from ..models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):

    form = PatientForm

    search_fields = ['subject_identifier']

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'initials',
                'dob',
                'gender',
                'protocols',
            ]}), audit_fieldset_tuple)

    radio_fields = {
        'gender': admin.VERTICAL}

    filter_horizontal = ('protocols', )

    list_display = (
        'subject_identifier',
        'gender',
        'initials',
        'dob',
    )

    list_filter = (
        'gender',
        'created',
    )
