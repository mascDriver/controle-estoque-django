from django.urls import path, re_path
from .views import *


urlpatterns = [
  path('', ListVendaView.as_view(), name='venda-list'),
  re_path(r'venda-add/$', CreateVendaView.as_view(), name='venda-add'),
  re_path(r'venda-detail/(?P<pk>[-\w]+)', DetailVendaView.as_view(), name='venda-detail'),
  re_path(r'venda-update/(?P<pk>[-\w]+)', UpdateVendaView.as_view(), name='venda-update'),
  re_path(r'^relatorio/$', relatorio_vendas, name='relatorio-vendas'),
]
