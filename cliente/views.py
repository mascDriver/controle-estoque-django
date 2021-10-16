from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import FormMixin, FormView
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Cliente
from .forms import ClienteForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class CreateClienteView(LoginRequiredMixin, CreateView):
    model = Cliente
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    form_class = ClienteForm
    template_name = 'clientes/form_cliente.html'


class ListClienteView(LoginRequiredMixin, ListView):
    model = Cliente
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    paginate_by = 5
    ordering = 'nome_cliente'
    template_name = 'clientes/list_clientes.html'

    def get_queryset(self):
        nome_cliente = self.request.GET.get('q_produto', '')
        object_list = self.model.objects.all().order_by('nome_cliente')
        if nome_cliente:
            object_list = object_list.filter(nome_cliente__icontains=nome_cliente)
        return object_list


class DetailClienteView(LoginRequiredMixin, DetailView, FormMixin):
    model = Cliente
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'clientes/detail_cliente.html'
    form_class = ClienteForm

    def get_success_url(self):
        return reverse('cliente_detail', kwargs={'pk': self.object.id})


class UpdateClienteView(LoginRequiredMixin, UpdateView):
    model = Cliente
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'clientes/detail_cliente.html'
    form_class = ClienteForm
