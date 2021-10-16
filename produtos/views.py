from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic.edit import FormMixin, FormView
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Produto
from .forms import ProdutoForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse


class CreateProductView(LoginRequiredMixin, CreateView):
    model = Produto
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    form_class = ProdutoForm
    template_name = 'produtos/form_produto.html'


class ListProductView(LoginRequiredMixin, ListView):
    model = Produto
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    paginate_by = 5
    ordering = 'cod_produto'
    template_name = 'produtos/list_products.html'

    def get_queryset(self):
        nome_produto = self.request.GET.get('q_produto', '')
        object_list = self.model.objects.all().order_by('cod_produto')
        if nome_produto:
            object_list = object_list.filter(nome_produto__icontains=nome_produto)
        return object_list


class DetailProductView(LoginRequiredMixin, DetailView, FormMixin):
    model = Produto
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'produtos/detail_products.html'
    form_class = ProdutoForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.id})


class UpdateProductView(LoginRequiredMixin, UpdateView):
    model = Produto
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'produtos/detail_products.html'
    form_class = ProdutoForm


def get_value_product(request, pk):
    product = Produto.objects.get(pk=pk)
    return JsonResponse({'value': product.valor_unit})
