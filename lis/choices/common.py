from django.utils.translation import ugettext_lazy as _


POS_NEG_UNKNOWN = (
    ('POS', _('Positive')),
    ('NEG', _('Negative')),
    ('UNKNOWN', _('Unknown')),
)

ART_STATUS_UNKNOWN = (
    ('ON', 'ON ART'),
    ('STOPPED', 'Stopped'),
    ('NAIVE', 'Naive'),
    ('UNKNOWN', 'Unknown'),
)

GENDER = (
    ('M', _('Male')),
    ('F', _('Female')),
)

ABS_CALC = (
    ('absolute', 'Absolute'),
    ('calculated', 'Calculated'),
    )

UNITS = (
    ('%', '%'),
    ('10^0/L', '10^0/L'),
    ('10^3/uL', '10^3/uL'),
    ('10^6/uL', '10^6/uL'),
    ('cells/ul', 'cells/ul'),
    ('copies/ml', 'copies/ml'),
    ('fL', 'fL'),
    ('g/dL', 'g/dL'),
    ('g/L', 'g/L'),
    ('mg/dL', 'mg/dL'),
    ('mg/L', 'mg/L'),
    ('mm^3', 'mm^3'),
    ('mm/H', 'mm/H'),
    ('mmol/L', 'mmol/L'),
    ('ng/ml', 'ng/ml'),
    ('pg', 'pg'),
    ('ratio', 'ratio'),
    ('U/L', 'U/L'),
    ('umol/L', 'umol/L'),
)

QUALIFIER = (
    ('=', '='),
    ('<', '<'),
    ('>', '>'),
)
