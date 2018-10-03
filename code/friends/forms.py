from django.forms import (
    Form, DateField, EmailField, CharField, Textarea, TextInput, IntegerField
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div, Field
from django.utils.translation import ugettext_lazy as _


class CreateContractForm(Form):
    valid_until = DateField()
    accepter = EmailField()
    text = CharField(widget=Textarea)

    def __init__(self, *args, **kwargs):
        super(CreateContractForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.wrapper_class = 'row'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-8'
        self.helper.layout = Layout(
            'valid_until',
            'accepter',
            'text',
            Submit('create', _('Create'), css_class="btn btn-primary"),
            HTML(
                '<a role="button" class="btn btn-warning" href="{%% url "contracts:list" %%}">%s</a>' %
                (_('Cancel'))
            ),
        )


class UpdateContractForm(Form):
    seqno = IntegerField(
        label="SeqNo",
        required=False,
        widget=TextInput(attrs={'readonly': 'readonly', 'disabled': True}),
    )
    version = IntegerField(
        label='Version',
        required=False,
        widget=TextInput(attrs={'readonly': 'readonly', 'disabled': True}),
    )
    valid_until = DateField()
    accepter = EmailField()
    text = CharField(widget=Textarea)

    def __init__(self, *args, **kwargs):
        super(UpdateContractForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.wrapper_class = 'row'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            'seqno',
            'version',
            'valid_until',
            'accepter',
            'text',
            Submit('update', _('Update'), css_class="btn btn-success"),
            Submit('release', _('Release'), css_class="btn btn-primary"),
            HTML(
                '<a role="button" class="btn btn-dark" href="{%% url "contracts:list" %%}">%s</a>' %
                (_('Cancel'))
            ),
        )
