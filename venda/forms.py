from django import forms
from .models import Venda, ItensVenda
from cliente.models import Cliente
from django.forms.models import inlineformset_factory
from django.core import validators
from django.core.exceptions import ValidationError
from produtos.models import Produto


class VendaForm(forms.ModelForm):
    data_venda = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'format': 'DD-MM-YYYY'}))
    valor_total_venda = forms.DecimalField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), )

    def __init__(self, *args, **kwargs):
        super(VendaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Venda
        fields = '__all__'


class ItensVendaForm(forms.ModelForm):
    valor_unit_venda = forms.DecimalField(label='Valor do produto', widget=forms.TextInput(attrs={'readonly': 'readonly'}), )
    cod_produto = forms.ModelChoiceField(label='Produto', queryset=Produto.objects.all().order_by('cod_produto'))

    def __init__(self, *args, **kwargs):
        super(ItensVendaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
            if field == 'valor_unit_venda':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control valor_unit_venda'
                })
            if field == 'quantidade':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control quantidade'
                })
            if field == 'cod_produto':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control produto'
                })

    class Meta:
        model = ItensVenda
        fields = '__all__'
        exclude = ['cod_venda']

    def clean(self):
        cleaned_data = super().clean()
        quantidade = cleaned_data['quantidade']
        produto = cleaned_data['cod_produto']
        if quantidade > produto.quantidade:
            raise ValidationError("Estoque insuficiente")
        return cleaned_data


VendaFormSet = inlineformset_factory(Venda, ItensVenda, form=ItensVendaForm, extra=1)

