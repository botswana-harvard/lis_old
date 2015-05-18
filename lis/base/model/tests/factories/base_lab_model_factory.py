import factory


class BaseLabModelFactory(factory.DjangoModelFactory):
    ABSTRACT_FACTORY = True
