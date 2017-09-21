from django.core.validators import RegexValidator
from django.db import models
from edc_base.model_mixins import BaseUuidModel
from edc_base.model_validators import date_not_future
from edc_constants.choices import GENDER
from edc_identifier.model_mixins import UniqueSubjectIdentifierModelMixin

from .protocol import Protocol

initials_validator = RegexValidator(
    regex=r'^[A-Z]{2,3}$',
    message='Ensure initials consist of letters only in upper case, no spaces.')


class Patient(UniqueSubjectIdentifierModelMixin, BaseUuidModel):

    initials = models.CharField(
        max_length=3,
        validators=[initials_validator])

    dob = models.DateField(
        verbose_name="Date of birth",
        validators=[date_not_future],
        help_text="Format is YYYY-MM-DD")

    gender = models.CharField(
        verbose_name="Gender",
        max_length=1,
        choices=GENDER)

    protocols = models.ManyToManyField(Protocol)

    def __str__(self):
        return self.subject_identifier
