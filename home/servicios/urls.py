from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_servicios, name='list_servicios'),
    path('create/', views.create_servicio, name='create_servicio'),
    path('update/<int:pk>/', views.update_servicio, name='update_servicio'),
    path('delete/<int:pk>/', views.delete_servicio, name='delete_servicio'),
    path('instalaciones/', views.list_instalaciones, name='list_instalaciones'),
    path('instalaciones/create/', views.create_instalacion, name='create_instalacion'),
    path('instalaciones/update/<int:pk>/', views.update_instalacion, name='update_instalacion'),
    path('instalaciones/delete/<int:pk>/', views.delete_instalacion, name='delete_instalacion'),
]
