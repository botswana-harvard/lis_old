try:
    from edc.device.sync.models import BaseSyncUuidModel as BaseUuidModel
except ImportError:
    from edc_base.model.models import BaseUuidModel


class BaseLabListUuidModel(BaseUuidModel):

    class Meta:
        abstract = True
