from edc_base.utils import round_up, get_age_in_days

from ..models import TestCodeReferenceListItem


def calculate_reference_range_comment(value, oResultItem):

    """ Calculate the reference range comment for a given test_code, value,
    gender and date of birth. Response comment is LO, HI, or PANIC
    Return a dictionary of comments
    """

    REFLIST = 'BHPLAB_NORMAL_RANGES_201005'

    result_value = value
    test_code = oResultItem.test_code
    receive = oResultItem.result.order.aliquot.receive
    patient = oResultItem.result.order.aliquot.receive.patient
    # get age in days using the collection date as a reference
    age_in_days = get_age_in_days(receive.datetime_drawn, patient.dob)

    # filter for the reference items for this list and this testcode, gender
    test_code_reference_list_item = TestCodeReferenceListItem.objects.filter(
                                    test_code_reference_list__name__iexact=REFLIST,
                                    test_code=test_code,
                                    gender__icontains=patient.gender,
                                    )
    comment = {}
    comment['low'] = ''
    comment['high'] = ''
    comment['panic_low'] = ''
    comment['panic_high'] = ''

    if test_code_reference_list_item:
        for reference_item in test_code_reference_list_item:
            # find the record for this age
            if reference_item.age_low_days() <= age_in_days and reference_item.age_high_days() >= age_in_days:
                # see if value is out of range
                # low? compare with correct decimal places
                if round_up(result_value, test_code.display_decimal_places) < round_up(reference_item.lln, test_code.display_decimal_places):
                    comment['low'] = 'LO'
                # high? compare with correct decimal places
                if round_up(result_value, test_code.display_decimal_places) > round_up(reference_item.uln, test_code.display_decimal_places):
                    comment['high'] = 'HI'
                # if result_value > reference.uln:
                #    comment['panic']='HI'
                # panic?
    return comment
