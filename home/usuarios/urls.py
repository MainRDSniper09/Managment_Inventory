from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.edit_profile, name='update_profile'),
    path('cliente/<int:pk>', views.cliente_detail, name='cliente_detail'),
    path('repartidor/<int:pk>', views.repartidor_detail, name='repartidor_detail'),
    path('administrativo/<int:pk>', views.administrativo_detail, name='administrativo_detail'),
    path('miembro_cuadrilla/<int:pk>', views.miembros_cuadrilla_detail, name='miembros_cuadrilla_detail'),
]