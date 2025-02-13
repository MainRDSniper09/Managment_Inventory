from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UsuarioCreationForm,  UsuarioChangeForm
from .models import Cliente, Repartidor, MiembroCuadrilla, Administrativo


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UsuarioCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'usuarios/profile.html')

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UsuarioChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UsuarioChangeForm(instance=request.user)
    return render(request, 'usuarios/update_profile.html', {'form': form})

@login_required
def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'usuarios/cliente_detail.html', {'cliente': cliente})

@login_required
def repartidor_detail(request, pk):
    repartidor = get_object_or_404(Repartidor, pk=pk)
    return render(request, 'usuarios/repartidor_detail.html', {'repartidor': repartidor})
@login_required
def miembro_cuadrilla_detail(request, pk):
    miembro_cuadrilla = get_object_or_404(MiembroCuadrilla, pk=pk)
    return render(request, 'usuarios/miembro_cuadrilla_detail.html', {'miembro_cuadrilla': miembro_cuadrilla})

@login_required
def administrativo_detail(request, pk):
    administrativo = get_object_or_404(Administrativo, pk=pk)
    return render(request, 'usuarios/administrativo_detail.html', {'administrativo': administrativo})