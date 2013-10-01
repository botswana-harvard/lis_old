import factory
from edc.lab.base.model.tests.factories import BaseLabModelFactory


class BaseTestCodeGroupFactory(BaseLabModelFactory):
    ABSTRACT_FACTORY = True

    code = factory.Sequence(lambda n: 'CODE{0}'.format(n))
    name = factory.Sequence(lambda n: 'NAME{0}'.format(n))
