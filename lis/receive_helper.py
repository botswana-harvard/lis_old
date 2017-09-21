from django.apps import apps as django_apps
from edc_base.utils import age
from edc_base.exceptions import AgeValueError

from .identifiers import ReceiveIdentifier


class ReceiveHelper:

    receive_identifier_cls = ReceiveIdentifier

    def __init__(self, receive_identifier=None, collection_datetime=None, dob=None):
        self.receive_identifier = receive_identifier
        if not self.receive_identifier:
            self.receive_identifier = self.receive_identifier_cls().identifier
        try:
            self.age = age(born=dob, reference_dt=collection_datetime)
        except AgeValueError:
            self.age = type('Age', (object, ), {'years': None})()

    @property
    def patient_model_cls(self):
        return django_apps.get_model(self.patient_model)
