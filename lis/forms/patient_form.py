from django import forms
from edc_base.modelform_validators import FormValidatorMixin

from ..form_validators import PatientFormValidator
from ..models import Patient


class PatientForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = PatientFormValidator

    class Meta:
        model = Patient
        fields = '__all__'
