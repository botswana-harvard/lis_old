from dateutil.relativedelta import relativedelta
from django.test import TestCase, tag
from edc_base.utils import get_utcnow
from edc_constants.constants import MALE
from edc_base.preload_data import PreloadData

from ..list_data import list_data
from ..models import Receive, Patient, SpecimenType, SpecimenCondition, Protocol


class TestReceiveModel(TestCase):

    def setUp(self):
        PreloadData(list_data=list_data)
        self.protocol_number = 'BHP999'
        Protocol.objects.create(name=self.protocol_number)
        self.subject_identifier = '12345'
        self.initials = 'NC'
        self.gender = MALE
        self.patient = Patient.objects.create(
            subject_identifier=self.subject_identifier,
            dob=get_utcnow().date() - relativedelta(years=25),
            gender=self.gender)

    def test_creates_receive_identifier(self):
        obj = Receive.objects.create(
            patient=self.patient,
            collection_datetime=get_utcnow() - relativedelta(days=1),
            protocol_number=self.protocol_number,
            specimen_type=SpecimenType.objects.all()[0],
            specimen_condition=SpecimenCondition.objects.all()[0])
        self.assertIsNotNone(obj.receive_identifier)

    def test_creates_receive_identifier_only_once(self):
        obj = Receive.objects.create(
            patient=self.patient,
            collection_datetime=get_utcnow() - relativedelta(days=1),
            protocol_number=self.protocol_number,
            specimen_type=SpecimenType.objects.all()[0],
            specimen_condition=SpecimenCondition.objects.all()[0])
        receive_identifier = obj.receive_identifier
        obj.save()
        self.assertEqual(receive_identifier, obj.receive_identifier)

    def test_does_not_create_receive_identifier_if_provided(self):
        obj = Receive.objects.create(
            receive_identifier='12345',
            patient=self.patient,
            collection_datetime=get_utcnow() - relativedelta(days=1),
            protocol_number=self.protocol_number,
            specimen_type=SpecimenType.objects.all()[0],
            specimen_condition=SpecimenCondition.objects.all()[0])
        self.assertEqual('12345', obj.receive_identifier)
