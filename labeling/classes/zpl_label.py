from .label import Label


class ZplLabel(Label):
    """A label class that takes a ZplTemplate instance to determine the template.

    Args:
      zpl_template: an instance of model ZplTemplate
      printer: a printer instance that is a base class of lis.labelling.classes.printer
    """
    def __init__(self, zpl_template, printer):
        super(ZplLabel, self).__init__(template=zpl_template.template, printer=printer)
