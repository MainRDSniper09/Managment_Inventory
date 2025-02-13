from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Bodega
from .forms import ProductoForm, BodegaForm

# Create your views here.
@login_required
def list_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/list_productos.html', {'productos': productos})

@login_required
def create_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_productos')
    else:
        form = ProductoForm()
    return render(request, 'productos/create_producto.html', {'form': form})

@login_required
def update_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('list_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/update_producto.html', {'form': form})

@login_required
def delete_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('list_productos')
    return render(request, 'productos/delete_producto.html', {'producto': producto})

@login_required
def list_bodegas(request):
    bodegas = Bodega.objects.all()
    return render(request, 'productos/list_bodegas.html', {'bodegas': bodegas})

@login_required
def create_bodega(request):
    if request.method == 'POST':
        form = BodegaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_bodegas')
    else:
        form = BodegaForm()
    return render(request, 'productos/create_bodega.html', {'form': form})

@login_required
def update_bodega(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    if request.method == 'POST':
        form = BodegaForm(request.POST, instance=bodega)
        if form.is_valid():
            form.save()
            return redirect('list_bodegas')
    else:
        form = BodegaForm(instance=bodega)
    return render(request, 'productos/update_bodega.html', {'form': form})

@login_required
def delete_bodega(request, pk):
    bodega = get_object_or_404(Bodega, pk=pk)
    if request.method == 'POST':
        bodega.delete()
        return redirect('list_bodegas')
    return render(request, 'productos/delete_bodega.html', {'bodega': bodega})