from django.urls import path # Importamos path para indicar las rutas
from . import views # Importamos views

# Lista de rutas
urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'), # Ruta principal
    path('staff/', views.staff, name='dashboard-staff'), # Ruta staff
    path('product/', views.product, name='dashboard-product'), # Ruta Productos
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'), # Ruta para Productos eliminados
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'), # Ruta para Productos editados  
    path('order/', views.order, name='dashboard-order'), # Ruta Orden
]


