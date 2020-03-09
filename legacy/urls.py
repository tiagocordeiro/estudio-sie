from django.urls import path

from . import views

urlpatterns = [
    path('os/', views.legacy_os_list, name='legacy_os_list'),
    path('clientes/', views.legacy_clientes_list, name='legacy_clientes_list'),
    path('cliente/<cli_codigo>/', views.legacy_customer_detail, name='legacy_customer_detail')
]
