from django import forms
from .models import Cliente
from django.core import validators


class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Cliente
        fields = '__all__'
