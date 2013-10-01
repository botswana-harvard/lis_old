import factory
from edc.lab.base.model.tests.factories import BaseLabUuidModelFactory


class BaseAliquotFactory(BaseLabUuidModelFactory):
    ABSTRACT_FACTORY = True

    aliquot_identifier = factory.Sequence(lambda n: n.rjust(15, '0'))
