from django.shortcuts import reverse
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Fornecedor
from .forms import FornecedorForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class CreateFornecedorView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Fornecedor
    form_class = FornecedorForm
    template_name = 'fornecedor/form_fornecedor.html'


class ListFornecedorView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Fornecedor
    paginate_by = 5
    ordering = 'cnpj'
    template_name = 'fornecedor/list_fornecedor.html'

    def get_queryset(self):
        nome_fantasia = self.request.GET.get('q_produto', '')
        object_list = self.model.objects.all().order_by('cnpj')
        if nome_fantasia:
            object_list = object_list.filter(nome_fantasia__icontains=nome_fantasia)
        return object_list


class DetailFornecedorView(LoginRequiredMixin, DetailView, FormMixin):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Fornecedor
    template_name = 'fornecedor/detail_fornecedor.html'
    form_class = FornecedorForm

    def get_success_url(self):
        return reverse('fornecedor-detail', kwargs={'pk': self.object.id})


class UpdateFornecedorView(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Fornecedor
    template_name = 'fornecedor/form_fornecedor.html'
    form_class = FornecedorForm
