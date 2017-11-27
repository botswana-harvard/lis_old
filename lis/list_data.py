from edc_base.preload_data import PreloadData
from .constants import CONDITION_OK


list_data = {
    'lis.specimentype': [
        ('WB', 'Whole Blood'),
    ],
    'lis.specimencondition': [
        (CONDITION_OK, 'OK'),
    ]}

model_data = {}
unique_field_data = {}

preload_data = PreloadData(
    list_data=list_data,
    model_data=model_data,
    unique_field_data=unique_field_data)
