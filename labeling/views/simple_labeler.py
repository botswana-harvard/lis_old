from django.shortcuts import render_to_response
from django.template import RequestContext

from ..classes import Label
from ..forms import LabelForm


def simple_labeler(request, **kwargs):

    template = 'label.html'
    if request.method == 'POST':
        form = LabelForm(request.POST)
        if form.is_valid():
            specimen_identifier = form.cleaned_data['identifier']
            try:
                label = Label(client_ip='127.0.0.1',
                              specimen_identifier=specimen_identifier,
                              template_name='simple_label',)
                label.print_label()
            except ValueError, err:
                raise ValueError('Unable to print, is the lab_barcode app configured? %s' % (err,))
        form = LabelForm()
    else:
        form = LabelForm()
    return render_to_response(template, {'form': form}, context_instance=RequestContext(request))
