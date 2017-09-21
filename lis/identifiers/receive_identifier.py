from edc_identifier.simple_identifier import SimpleSequentialIdentifier


class ReceiveIdentifierError(Exception):
    pass


class ReceiveIdentifier(SimpleSequentialIdentifier):

    prefix = 'R'
