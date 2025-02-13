from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_cuadrillas, name='list_cuadrillas'),
    path('create/', views.create_cuadrilla, name='create_cuadrilla'),
    path('update/<int:pk>/', views.update_cuadrilla, name='update_cuadrilla'),
    path('delete/<int:pk>/', views.delete_cuadrilla, name='delete_cuadrilla'),
    path('asignaciones/', views.list_asignaciones, name='list_asignaciones'),
    path('asignaciones/create/', views.create_asignacion, name='create_asignacion'),
    path('asignaciones/update/<int:pk>/', views.update_asignacion, name='update_asignacion'),
    path('asignaciones/delete/<int:pk>/', views.delete_asignacion, name='delete_asignacion'),
]
