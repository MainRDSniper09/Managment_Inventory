from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


@login_required # Se necesita loguearse para poder ver las demas rutas
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders': orders,
        'form' : form,
        'products': products,
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = User.objects.count()
    orders_count = Order.objects.count()  
    products_count = Product.objects.count()  

    context = {
        'workers': workers,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count': products_count,
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    workers = User.objects.get(id=pk)
    context ={
        'workers': workers,
    }  
    return render(request, 'dashboard/staff_detail.html', context)

@login_required # Se necesita loguearse para poder ver las demas rutas
def product(request):
    items = Product.objects.all() # Usando el ORM
    products_count = items.count()
    # items = Product.objects.raw('SELECT * FROM dashboard_product') # Sentencia sql para seleccionar todos los productos
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    
    if request.method == 'POST': # Comprobacion para guardar nuevos objetos dentro de nuestra db
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} fue añadido')
            
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    context ={
        'items': items,
        'form': form,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count' : products_count,

    }
    return render(request, 'dashboard/product.html', context)

@login_required
def product_delete(request, pk): # Recibimos la llave primaria para eliminar
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk): # Metodo para modificar un producto
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)

@login_required # Se necesita loguearse para poder ver las demas rutas
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    products_count = Product.objects.all().count()
    context = {
        'orders': orders,
        'workers_count': workers_count,
        'orders_count': orders_count,
        'products_count': products_count,
    }
    return render(request, 'dashboard/order.html', context)


