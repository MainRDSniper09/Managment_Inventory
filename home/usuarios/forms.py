from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Cliente, Repartidor, MiembroCuadrilla, Administrativo

#Creacion usuarios
class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'tipo_usuario')

#Actualizacion Usuario
class UsuarioChangeForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'tipo_usuario')

#Manejo datos segun mi tipo de usuario (cambiar si lo consideras)
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('direccion', 'ciudad','codigo_postal')

class RepartidorForm(forms.ModelForm):
    class Meta:
        model = Repartidor
        fields = ('disponibilidad','bodega')

class MiembroCuadrillaForm(forms.ModelForm):
    class Meta:
        model = MiembroCuadrilla
        fields = ('cuadrilla', 'rol')
class AdministrativoForm(forms.ModelForm):
    class Meta:
        model = Administrativo
        fields = ('departamento',)
