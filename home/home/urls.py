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
from django.contrib.auth import views as auth_views # Importamos la autenticacion
from django.conf import settings # Importamos configuraciones para archivos estaticos
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')), # Ruta principal
    path('register/', user_view.register, name='user-register'), # Ruta para el registro de usuarios
     path('profile/', user_view.profile, name='user-profile'), # Ruta para el registro de usuarios
    path('', auth_views.LoginView.as_view(template_name='user/login.html'),name='user-login'), # Creamos la ruta de login
    # TODO encontrar el porque no muestra pagina logout.html
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'), # Creamos pagina de deslogeo
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
