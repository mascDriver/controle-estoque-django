from django.urls import path, re_path
from .views import *


urlpatterns = [
  path('', ListClienteView.as_view(), name='cliente-list'),
  re_path(r'cliente-add/$', CreateClienteView.as_view(), name='cliente-add'),
  re_path(r'cliente-detail/(?P<pk>[-\w]+)', DetailClienteView.as_view(), name='cliente-detail'),
  re_path(r'cliente-update/(?P<pk>[-\w]+)', UpdateClienteView.as_view(), name='cliente-update')
]
