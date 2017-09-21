from django import forms
from edc_base.modelform_validators import FormValidator
from edc_base.modelform_validators.base_form_validator import REQUIRED_ERROR

INVALID_PROTOCOL = 'Invalid protocol'


class ReceiveFormValidator(FormValidator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.protocol_number = self.cleaned_data.get('protocol_number')
        self.patient = self.cleaned_data.get('patient')

    def clean(self):
        if not self.patient:
            raise forms.ValidationError(
                {'patient': 'This field is required.'}, code=REQUIRED_ERROR)
        if self.protocol_number not in [obj.name for obj in self.patient.protocols.all()]:
            raise forms.ValidationError(
                {'protocol_number': 'Invalid protocol number for patient.'},
                code=INVALID_PROTOCOL)
