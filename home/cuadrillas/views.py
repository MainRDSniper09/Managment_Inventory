from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cuadrilla, AsignacionCuadrilla
from .forms import CuadrillaForm, AsignacionCuadrillaForm

# Create your views here.
@login_required
def list_cuadrillas(request):
    cuadrillas = Cuadrilla.objects.all()
    return render(request, 'cuadrillas/list_cuadrillas.html', {'cuadrillas': cuadrillas})

@login_required
def create_cuadrilla(request):
    if request.method == 'POST':
        form = CuadrillaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_cuadrillas')
    else:
        form = CuadrillaForm()
    return render(request, 'cuadrillas/create_cuadrilla.html', {'form': form})

@login_required
def update_cuadrilla(request, pk):
    cuadrilla = get_object_or_404(Cuadrilla, pk=pk)
    if request.method == 'POST':
        form = CuadrillaForm(request.POST, instance=cuadrilla)
        if form.is_valid():
            form.save()
            return redirect('list_cuadrillas')
    else:
        form = CuadrillaForm(instance=cuadrilla)
    return render(request, 'cuadrillas/update_cuadrilla.html', {'form': form})

@login_required
def delete_cuadrilla(request, pk):
    cuadrilla = get_object_or_404(Cuadrilla, pk=pk)
    if request.method == 'POST':
        cuadrilla.delete()
        return redirect('list_cuadrillas')
    return render(request, 'cuadrillas/delete_cuadrilla.html', {'cuadrilla': cuadrilla})

@login_required
def list_asignaciones(request):
    asignaciones = AsignacionCuadrilla.objects.all()
    return render(request, 'cuadrillas/list_asignaciones.html', {'asignaciones': asignaciones})

@login_required
def create_asignacion(request):
    if request.method == 'POST':
        form = AsignacionCuadrillaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_asignaciones')
    else:
        form = AsignacionCuadrillaForm()
    return render(request, 'cuadrillas/create_asignacion.html', {'form': form})

@login_required
def update_asignacion(request, pk):
    asignacion = get_object_or_404(AsignacionCuadrilla, pk=pk)
    if request.method == 'POST':
        form = AsignacionCuadrillaForm(request.POST, instance=asignacion)
        if form.is_valid():
            form.save()
            return redirect('list_asignaciones')
    else:
        form = AsignacionCuadrillaForm(instance=asignacion)
    return render(request, 'cuadrillas/update_asignacion.html', {'form': form})

@login_required
def delete_asignacion(request, pk):
    asignacion = get_object_or_404(AsignacionCuadrilla, pk=pk)
    if request.method == 'POST':
        asignacion.delete()
        return redirect('list_asignaciones')
    return render(request, 'cuadrillas/delete_asignacion.html', {'asignacion': asignacion})



