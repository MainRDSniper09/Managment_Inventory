from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('productos/', views.productos_lista, name='productos_lista'),
    path('servicios/', views.servicios_lista, name='servicios_lista'),
    path('insumos/', views.insumos_lista, name='insumos_lista'),
    path('pedidos/', views.pedidos_lista, name='pedidos_lista'),
    path('cuadrillas/', views.cuadrillas_lista, name='cuadrillas_lista'),
    path('notificaciones/', views.notificaciones_lista, name='notificaciones_lista'),
]
