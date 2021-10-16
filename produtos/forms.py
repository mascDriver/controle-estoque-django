from django import forms
from .models import Produto
from django.core import validators


class ProdutoForm(forms.ModelForm):
    quantidade = forms.IntegerField(validators=[validators.MinValueValidator(0)])

    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Produto
        fields = '__all__'
