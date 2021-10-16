from django.urls import path, re_path
from .views import *


urlpatterns = [
  path('', ListUsuarioView.as_view(), name='usuario-list'),
  re_path(r'usuario-add/$', CreateUsuarioView.as_view(), name='usuario-add'),
  re_path(r'usuario-detail/(?P<pk>[-\w]+)', DetailUsuarioView.as_view(), name='usuario-detail'),
  re_path(r'usuario-update/(?P<pk>[-\w]+)', UpdateUsuarioView.as_view(), name='usuario-update'),
  path(r'logout', logout_page, name='usuario-logout'),
  # path('login/', LoginView.as_view(), name='login'),

]
