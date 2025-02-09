"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Importamos include para incluir las rutas de las aplicaciones
from user import views as user_view # Importamos las vistas de la aplicacion user


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')), # Ruta principal
    path('register/', user_view.register, name='user-register'), # Ruta para el registro de usuarios
]
