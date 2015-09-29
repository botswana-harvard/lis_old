from edc_constants.constants import PENDING, PARTIAL, COMPLETE, ERROR

ORDER_STATUS = (
    (PENDING, 'Pending'),
    (PARTIAL, 'Partial'),
    (COMPLETE, 'Complete'),
    (ERROR, 'Error'),
    ('REDRAW', 'Redraw'),
    ('WITHDRAWN', 'Withdrawn'),
    ('DUPLICATE', 'Duplicate'),
)
