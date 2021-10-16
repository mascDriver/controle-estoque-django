from django.urls import path, re_path
from .views import *


urlpatterns = [
  path('', ListFornecedorView.as_view(), name='fornecedor-list'),
  re_path(r'fornecedor-add/$', CreateFornecedorView.as_view(), name='fornecedor-add'),
  re_path(r'fornecedor-detail/(?P<pk>[-\w]+)', DetailFornecedorView.as_view(), name='fornecedor-detail'),
  re_path(r'fornecedor-update/(?P<pk>[-\w]+)', UpdateFornecedorView.as_view(), name='fornecedor-update')
]
