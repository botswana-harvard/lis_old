import factory


class BaseLabUuidModelFactory(factory.DjangoModelFactory):
    ABSTRACT_FACTORY = True

    @classmethod
    def _setup_next_sequence(cls):
        try:
            return 1 + cls._associated_class._default_manager.count()
        except IndexError:
            return 1
