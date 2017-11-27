from django import forms
from edc_form_validators import FormValidatorMixin

from ..form_validators import ReceiveFormValidator
from ..models import Receive


class ReceiveForm(FormValidatorMixin, forms.ModelForm):

    form_validator_cls = ReceiveFormValidator

    class Meta:
        model = Receive
        fields = '__all__'
