from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import ChecklistInsumo, Insumo
from servicios.models import InstalacionServicio
from .forms import InsumoForm, ChecklistInsumoForm

@login_required
def list_insumos(request):
    insumos = Insumo.objects.all()
    return render(request, 'insumos/list_insumos.html', {'insumos': insumos})

@login_required
def create_insumo(request):
    if request.method == 'POST':
        form = InsumoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_insumos')
    else:
        form = InsumoForm()
    return render(request, 'insumos/create_insumo.html', {'form': form})

@login_required
def update_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    if request.method == 'POST':
        form = InsumoForm(request.POST, instance=insumo)
        if form.is_valid():
            form.save()
            return redirect('list_insumos')
    else:
        form = InsumoForm(instance=insumo)
    return render(request, 'insumos/update_insumo.html', {'form': form})

@login_required
def delete_insumo(request, pk):
    insumo = get_object_or_404(Insumo, pk=pk)
    if request.method == 'POST':
        insumo.delete()
        return redirect('list_insumos')
    return render(request, 'insumos/delete_insumo.html', {'insumo': insumo})

# Create your views here.

def checklist_insumo_list(request, instalacion_id):
    instalacion = get_object_or_404(InstalacionServicio, id=instalacion_id)
    insumos = Insumo.objects.filter(bodega=instalacion.cuadrilla.bodega)

    if request.method == 'POST':
        form = ChecklistInsumoForm(request.POST)
        if form.is_valid():
            checklist = form.save(commit=False)
            checklist.instalacion = instalacion
            checklist.miembro_cuadrilla = request.user.miembrocuadrilla
            checklist.save()
            return redirect('insumos:checklist_success')
    else:
        form = ChecklistInsumoForm()

    return render(request, 'insumos/checklist_insumo.html',
                  {'form': form, 'insumos': insumos, 'instalacion': instalacion})

def checklist_success(request):
    return render(request, 'insumos/checklist_success.html')