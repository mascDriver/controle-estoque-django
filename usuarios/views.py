from django.shortcuts import reverse, render
from django.views.generic.edit import FormMixin
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import logout


class CreateUsuarioView(LoginRequiredMixin, CreateView):
    model = Usuario
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    form_class = NewUserForm
    template_name = 'usuario/form_usuario.html'


class ListUsuarioView(LoginRequiredMixin, ListView):
    model = Usuario
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    paginate_by = 5
    ordering = 'cod_usuario'
    template_name = 'usuario/list_usuario.html'

    def get_queryset(self):
        nome_fantasia = self.request.GET.get('q_produto', '')
        object_list = self.model.objects.all().order_by('cod_usuario')
        if nome_fantasia:
            object_list = object_list.filter(nome_fantasia__icontains=nome_fantasia)
        return object_list


class DetailUsuarioView(LoginRequiredMixin, DetailView, FormMixin):
    model = Usuario
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'usuario/detail_usuario.html'
    form_class = NewUserForm

    def get_success_url(self):
        return reverse('usuario-detail', kwargs={'pk': self.object.id})


class UpdateUsuarioView(LoginRequiredMixin, UpdateView):
    model = Usuario
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    template_name = 'usuario/form_usuario.html'
    form_class = NewUserForm


def logout_page(request):
    context = {
        "content": "Você efetuou o logout com sucesso! :)"
    }
    logout(request)
    return render(request, "registration/logout.html", context)
