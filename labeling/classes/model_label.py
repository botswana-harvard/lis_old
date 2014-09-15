from django.contrib import messages

from .label import Label


class ModelLabel(Label):
    """ Print a label building the template and context from the model."""
    def __init__(self):
        super(ModelLabel, self).__init__()
        self._model_instance = None

    def test(self, client_addr):
        return super(ModelLabel, self).print_label(1, client_addr=client_addr, debug=True)

    def print_label(self, request, model_instance, copies=None, update_messages=True, client_addr=None):
        """Returns a tuple of success message, error message and boolean, by
        calling the base class print_label.

        Also updates django messages."""
        if request:
            client_addr = client_addr or request.META.get('REMOTE_ADDR')
        self.model_instance = model_instance
        copies = copies or 1
        msg, err_msg, print_success = super(ModelLabel, self).print_label(copies,
                                                                          client_addr=client_addr)
        if update_messages:
            if err_msg:
                messages.add_message(request, messages.ERROR, err_msg)
            if msg:
                messages.add_message(request, messages.SUCCESS, msg)
        return msg, err_msg, print_success

    @property
    def model_instance(self):
        return self._model_instance

    @model_instance.setter
    def model_instance(self, model_instance):
        """Sets the model instance and refreshes the label_context."""
        self._model_instance = model_instance
        self.refresh_label_context()

    def refresh_label_context(self):
        """ Add all the model fields to the template context for the current model instance."""
        self.label_context = {}
        for field in self.model_instance._meta.fields:
            value = getattr(self.model_instance, field.attname, field.attname)
            try:
                self.label_context.update({field.attname: value.strftime('%Y-%m-%d %H:%M')})
            except AttributeError:
                self.label_context.update({field.attname: value})
        self.label_context.update({'barcode_value': self.model_instance.barcode_value()})
        return True
