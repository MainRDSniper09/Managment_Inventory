from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Pedidos, DetallePedido
from .forms import PedidosForm, DetallePedidoForm

# Create your views here.
@login_required
def list_pedidos(request):
    pedidos = Pedidos.objects.all()
    return render(request, 'pedidos/list_pedidos.html', {'pedidos': pedidos})

@login_required
def create_pedido(request):
    if request.method == 'POST':
        form = PedidosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_pedidos')
    else:
        form = PedidosForm()
    return render(request, 'pedidos/create_pedido.html', {'form': form})

@login_required
def update_pedido(request, pk):
    pedido = get_object_or_404(Pedidos, pk=pk)
    if request.method == 'POST':
        form = PedidosForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('list_pedidos')
    else:
        form = PedidosForm(instance=pedido)
    return render(request, 'pedidos/update_pedido.html', {'form': form})

@login_required
def delete_pedido(request, pk):
    pedido = get_object_or_404(Pedidos, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('list_pedidos')
    return render(request, 'pedidos/delete_pedido.html', {'pedido': pedido})
@login_required
def list_detalles_pedido(request, pedido_id):
    detalles = DetallePedido.objects.filter(pedido_id=pedido_id)
    return render(request, 'pedidos/list_detalles_pedido.html', {'detalles': detalles, 'pedido_id': pedido_id})

@login_required
def create_detalle_pedido(request, pedido_id):
    if request.method == 'POST':
        form = DetallePedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_detalles_pedido', pedido_id=pedido_id)
    else:
        form = DetallePedidoForm(initial={'pedido': pedido_id})
    return render(request, 'pedidos/create_detalle_pedido.html', {'form': form, 'pedido_id': pedido_id})

@login_required
def update_detalle_pedido(request, pk):
    detalle = get_object_or_404(DetallePedido, pk=pk)
    if request.method == 'POST':
        form = DetallePedidoForm(request.POST, instance=detalle)
        if form.is_valid():
            form.save()
            return redirect('list_detalles_pedido', pedido_id=detalle.pedido.id)
    else:
        form = DetallePedidoForm(instance=detalle)
    return render(request, 'pedidos/update_detalle_pedido.html', {'form': form, 'pedido_id': detalle.pedido.id})

@login_required
def delete_detalle_pedido(request, pk):
    detalle = get_object_or_404(DetallePedido, pk=pk)
    pedido_id = detalle.pedido.id
    if request.method == 'POST':
        detalle.delete()
        return redirect('list_detalles_pedido', pedido_id=pedido_id)
    return render(request, 'pedidos/delete_detalle_pedido.html', {'detalle': detalle, 'pedido_id': pedido_id})


