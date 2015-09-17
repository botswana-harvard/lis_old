from django import forms

from ..models import ZplTemplate, LabelPrinter


class LabelForm(forms.ModelForm):

    identifier = forms.CharField(
        max_length=25,
        label="Identifier",
        help_text="",
        error_messages={'required': 'Please enter a valid identifier.'})


class ZplTemplateForm (forms.ModelForm):

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    class Meta:
        model = ZplTemplate


class LabelPrinterForm (forms.ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    class Meta:
        model = LabelPrinter
