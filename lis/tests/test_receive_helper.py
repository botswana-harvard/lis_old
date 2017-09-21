from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import MALE

from ..receive_helper import ReceiveHelper
from ..models import Patient


class TestReceiveHelper(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            subject_identifier='123456789',
            dob=get_utcnow().date() - relativedelta(years=25),
            gender=MALE)

    def test_creates_receive_identifier(self):
        helper = ReceiveHelper(
            dob=self.patient.dob,
            collection_datetime=get_utcnow() - relativedelta(days=1))
        self.assertIsNotNone(helper.receive_identifier)

    def test_does_not_create_receive_identifier_if_provided(self):
        helper = ReceiveHelper(
            dob=self.patient.dob,
            receive_identifier='12345',
            collection_datetime=get_utcnow() - relativedelta(days=1))
        self.assertEqual('12345', helper.receive_identifier)

    def test_age_at_receive(self):
        helper = ReceiveHelper(
            dob=self.patient.dob,
            collection_datetime=get_utcnow() - relativedelta(years=1))
        self.assertEqual(helper.age.years, 24)
