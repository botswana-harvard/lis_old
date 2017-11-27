from django.apps import apps as django_apps
from django.urls import reverse
from django.utils.safestring import mark_safe
from edc_constants.constants import YES
from edc_lab_dashboard.views import RequisitionListboardView

app_config = django_apps.get_app_config('edc_lab_dashboard')


class ReceiveListboardView(RequisitionListboardView):

    form_action_url = 'receive_listboard_url'
    listboard_template_name = 'receive_listboard_template'
    listboard_url = 'receive_listboard_url'
    navbar_item_selected = 'receive'
    show_all = True

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        options.update(
            {'is_drawn': YES, 'received': False, 'processed': False})
        return options

    @property
    def empty_queryset_message(self):
        href = reverse(self.process_listboard_url_name)
        return mark_safe(
            'All specimens have been received. Continue to '
            f'<a href="{href}" class="alert-link">processing</a>')
