from django.shortcuts import reverse, redirect, render
from django.views.generic.edit import FormMixin, FormView
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Venda
from .forms import VendaForm, VendaFormSet
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
import json
from django.db.models import Sum, Count
from django.core.serializers.json import DjangoJSONEncoder


class CreateVendaView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    form_class = VendaForm
    template_name = 'venda/form_venda.html'
    model = Venda

    def get_context_data(self, **kwargs):
        context = super(CreateVendaView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['forms'] = VendaForm(self.request.POST, instance=self.object)
            context['formset'] = VendaFormSet(self.request.POST, instance=self.object)
        else:
            context['forms'] = VendaForm(instance=self.object)
            context['formset'] = VendaFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        forms = context['forms']
        formset = context['formset']
        if forms.is_valid() and formset.is_valid():
            self.object = forms.save()
            forms.instance = self.object
            forms.save()
            formset.instance = self.object
            formset.save()
            return redirect('venda-list')
        else:
            return self.render_to_response(self.get_context_data(form=forms))


class ListVendaView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Venda
    paginate_by = 5
    ordering = 'cod_venda'
    template_name = 'venda/list_venda.html'

    def get_queryset(self):
        nome_fantasia = self.request.GET.get('q_produto', '')
        object_list = self.model.objects.all().order_by('cod_venda')
        if nome_fantasia:
            object_list = object_list.filter(nome_fantasia__icontains=nome_fantasia)
        return object_list


class DetailVendaView(LoginRequiredMixin, DetailView, FormMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Venda
    template_name = 'venda/detail_venda.html'
    form_class = VendaForm

    def get_success_url(self):
        return reverse('fornecedor-detail', kwargs={'pk': self.object.id})


class UpdateVendaView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Venda
    template_name = 'venda/form_venda.html'
    form_class = VendaForm

    def get_context_data(self, **kwargs):
        context = super(UpdateVendaView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['forms'] = VendaForm(self.request.POST, instance=self.object)
            context['formset'] = VendaFormSet(self.request.POST, instance=self.object)
        else:
            context['forms'] = VendaForm(instance=self.object)
            context['formset'] = VendaFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        forms = context['forms']
        formset = context['formset']
        if forms.is_valid() and formset.is_valid():
            self.object = form.save()
            forms.instance = self.object
            formset.instance = self.object
            forms.save()
            formset.save()
            return redirect('venda-list')
        else:
            return self.render_to_response(self.get_context_data(form=form))


def relatorio_vendas(request):

    return render(request, 'relatorios/pedidos.html', return_grapf())


def return_grapf():
    queryset = (Venda.objects.values('data_venda', 'valor_total_venda').annotate(dcount=Count('data_venda')).order_by('data_venda'))
    date = [obj['data_venda'].strftime('%d/%m/%Y') for obj in queryset]
    total = [obj['valor_total_venda'] for obj in queryset]

    queryset = (Venda.objects.values('data_venda').annotate(dcount=Count('data_venda')).order_by('data_venda'))
    dcount = [int(obj['dcount']) for obj in queryset]
    data_count = [(obj['data_venda'].strftime('%d/%m/%Y')) for obj in queryset]
    context = {
        'date': json.dumps(date, cls=DjangoJSONEncoder),
        'total': json.dumps(total, cls=DjangoJSONEncoder),
        'dcount': json.dumps(dcount, cls=DjangoJSONEncoder),
        'data_count': json.dumps(data_count, cls=DjangoJSONEncoder),
    }
    return context
