from datetime import datetime

from django.contrib import messages

from .label import Label


class ModelLabel(Label):
    """ Print a label building the template and context from the model."""
    def __init__(self):
        self._model_instance = None
        self.label_context = {}
        super(ModelLabel, self).__init__()

    def print_label(self, request, model_instance, copies=None):
        self.model_instance = model_instance
        if not self.zpl_template:
            self.zpl_template = self.default_template
        copies = copies or 1
        msg, success = super(ModelLabel, self).print_label(copies, request.META.get('REMOTE_ADDR'))
        if not success:
            messages.add_message(request, messages.ERROR, msg)
        else:
            messages.add_message(request, messages.SUCCESS, msg)

    @property
    def model_instance(self):
        return self._model_instance

    @model_instance.setter
    def model_instance(self, value):
        """Sets the model instance and refreshes the label_context."""
        self._model_instance = value
        self.refresh_label_context()

    def refresh_label_context(self):
        """ Add all the model fields to the template context for the current model instance."""
        self.label_context = {}
        for field in self.model_instance._meta.fields:
            if isinstance(getattr(self.model_instance, field.attname, field.attname), datetime):
                timestamp = getattr(self.model_instance, field.attname, field.attname).strftime('%Y-%m-%d %H:%M')
                self.label_context.update({field.attname: timestamp})
            else:
                self.label_context.update({field.attname: getattr(self.model_instance, field.attname, field.attname)})
        self.label_context.update({'barcode_value': self.model_instance.barcode_value()})

    @property
    def default_zpl_template_name(self):
        return '{0} Template'.format(self.model_instance._meta.object_name)
