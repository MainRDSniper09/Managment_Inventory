from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_productos, name='list_productos'),
    path('create/', views.create_producto, name='create_producto'),
    path('update/<int:pk>/', views.update_producto, name='update_producto'),
    path('delete/<int:pk>/', views.delete_producto, name='delete_producto'),
    path('bodegas/', views.list_bodegas, name='list_bodegas'),
    path('bodegas/create/', views.create_bodega, name='create_bodega'),
    path('bodegas/update/<int:pk>/', views.update_bodega, name='update_bodega'),
    path('bodegas/delete/<int:pk>/', views.delete_bodega, name='delete_bodega'),
]