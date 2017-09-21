from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import MALE

from ..models import Patient, Protocol


class TestReceive(TestCase):

    def setUp(self):
        Protocol.objects.create(name='BHP999')
        self.subject_identifier = '12345'
        self.initials = 'NC'
        self.gender = MALE

    def test_create(self):
        Patient.objects.create(
            subject_identifier=self.subject_identifier,
            dob=get_utcnow() - relativedelta(years=25),
            gender=self.gender)
