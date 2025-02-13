from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_pedidos, name='list_pedidos'),
    path('create/', views.create_pedido, name='create_pedido'),
    path('update/<int:pk>/', views.update_pedido, name='update_pedido'),
    path('delete/<int:pk>/', views.delete_pedido, name='delete_pedido'),
    path('detalles/<int:pedido_id>/', views.list_detalles_pedido, name='list_detalles_pedido'),
    path('detalles/create/<int:pedido_id>/', views.create_detalle_pedido, name='create_detalle_pedido'),
    path('detalles/update/<int:pk>/', views.update_detalle_pedido, name='update_detalle_pedido'),
    path('detalles/delete/<int:pk>/', views.delete_detalle_pedido, name='delete_detalle_pedido'),
]
