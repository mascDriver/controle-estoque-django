from django.urls import path, re_path
from .views import *


urlpatterns = [
  path('', ListProductView.as_view(), name='product-list'),
  re_path(r'product-add/$', CreateProductView.as_view(), name='product-add'),
  re_path(r'product-detail/(?P<pk>[-\w]+)', DetailProductView.as_view(), name='product-detail'),
  re_path(r'product-value/(?P<pk>[-\w]+)', get_value_product, name='product-value'),
  re_path(r'product-update/(?P<pk>[-\w]+)', UpdateProductView.as_view(), name='product-update')
]
