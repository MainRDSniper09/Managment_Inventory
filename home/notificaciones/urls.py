from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_notificaciones, name='list_notificaciones'),
    path('create/', views.create_notificacion, name='create_notificacion'),
    path('update/<int:pk>/', views.update_notificacion, name='update_notificacion'),
    path('delete/<int:pk>/', views.delete_notificacion, name='delete_notificacion'),
    path('marcar_como_leido/<int:pk>/', views.marcar_como_leido, name='marcar_como_leido'),
]
