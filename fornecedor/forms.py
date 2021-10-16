from django import forms
from .models import Fornecedor
from django.core import validators


class FornecedorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FornecedorForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Fornecedor
        fields = '__all__'
