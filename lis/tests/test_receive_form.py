from dateutil.relativedelta import relativedelta
from django.core.exceptions import ValidationError
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import MALE
from edc_base.preload_data import PreloadData

from ..form_validators import ReceiveFormValidator
from ..forms import ReceiveForm
from ..list_data import list_data
from ..models import Patient, Protocol


class TestReceiveForm(TestCase):

    def setUp(self):
        PreloadData(list_data=list_data)
        self.protocol_number = 'BHP999'
        Protocol.objects.create(name=self.protocol_number)
        self.subject_identifier = '12345'
        self.initials = 'NC'
        self.gender = MALE
        self.patient = Patient.objects.create(
            subject_identifier=self.subject_identifier,
            dob=get_utcnow() - relativedelta(years=25),
            gender=self.gender)

    def test_receive_validator_protocol(self):
        """Asserts patient must be linked to protocol number.
        """
        # no protocol number given
        cleaned_data = {'patient': self.patient}
        validator = ReceiveFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, validator.validate)
        self.assertIn('protocol_number', validator._errors)

        # protocol number given does not match with any of patient
        cleaned_data = {
            'patient': self.patient,
            'protocol_number': self.protocol_number}
        validator = ReceiveFormValidator(cleaned_data=cleaned_data)
        self.assertRaises(ValidationError, validator.validate)
        self.assertIn('protocol_number', validator._errors)

        # protocol number matches one of patient
        self.patient.protocols.add(
            Protocol.objects.create(name='BHP998'))
        self.patient.protocols.add(
            Protocol.objects.get(name='BHP999'))
        cleaned_data = {
            'patient': self.patient,
            'protocol_number': self.protocol_number}
        validator = ReceiveFormValidator(cleaned_data=cleaned_data)
        validator.validate()
        self.assertNotIn('protocol_number', validator._errors)

    def test_receive_validator_collection_datetime_not_future(self):
        self.patient.protocols.add(
            Protocol.objects.get(name='BHP999'))
        cleaned_data = {
            'patient': self.patient,
            'protocol_number': self.protocol_number,
            'collection_datetime': get_utcnow() + relativedelta(years=1)}
        form = ReceiveForm(data=cleaned_data)
        self.assertFalse(form.is_valid())
        self.assertIn('collection_datetime', form._errors)
