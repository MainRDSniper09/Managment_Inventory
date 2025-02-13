from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Servicio, InstalacionServicio, DetalleInstalacionServicio
from .forms import ServicioForm, InstalacionServicioForm, DetalleInstalacionServicioForm

@login_required
def list_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/list_servicios.html', {'servicios': servicios})

@login_required
def create_servicio(request):
    if request.method == 'POST':
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_servicios')
    else:
        form = ServicioForm()
    return render(request, 'servicios/create_servicio.html', {'form': form})

@login_required
def update_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            return redirect('list_servicios')
    else:
        form = ServicioForm(instance=servicio)
    return render(request, 'servicios/update_servicio.html', {'form': form})

@login_required
def delete_servicio(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == 'POST':
        servicio.delete()
        return redirect('list_servicios')
    return render(request, 'servicios/delete_servicio.html', {'servicio': servicio})

@login_required
def list_instalaciones(request):
    instalaciones = InstalacionServicio.objects.all()
    return render(request, 'servicios/list_instalaciones.html', {'instalaciones': instalaciones})

@login_required
def create_instalacion(request):
    if request.method == 'POST':
        form = InstalacionServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_instalaciones')
    else:
        form = InstalacionServicioForm()
    return render(request, 'servicios/create_instalacion.html', {'form': form})

@login_required
def update_instalacion(request, pk):
    instalacion = get_object_or_404(InstalacionServicio, pk=pk)
    if request.method == 'POST':
        form = InstalacionServicioForm(request.POST, instance=instalacion)
        if form.is_valid():
            form.save()
            return redirect('list_instalaciones')
    else:
        form = InstalacionServicioForm(instance=instalacion)
    return render(request, 'servicios/update_instalacion.html', {'form': form})

@login_required
def delete_instalacion(request, pk):
    instalacion = get_object_or_404(InstalacionServicio, pk=pk)
    if request.method == 'POST':
        instalacion.delete()
        return redirect('list_instalaciones')
    return render(request, 'servicios/delete_instalacion.html', {'instalacion': instalacion})

