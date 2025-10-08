from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Order, Hotel, Reservation
from .forms import ProductForm, OrderForm, ReservationForm, HotelFilterForm
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


@login_required
def client_portal(request):
    hotels = Hotel.objects.all()
    filter_form = HotelFilterForm(request.GET or None)

    if filter_form.is_valid():
        search = filter_form.cleaned_data.get('search')
        city = filter_form.cleaned_data.get('city')

        if search:
            hotels = hotels.filter(name__icontains=search)
        if city:
            hotels = hotels.filter(Q(city__icontains=city) | Q(country__icontains=city))

    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(
                request,
                'Tu reservación ha sido registrada. Recibirás un correo con la confirmación.',
            )
            return redirect('dashboard-client-portal')
    else:
        initial = {}
        selected_hotel = request.GET.get('hotel')
        if selected_hotel:
            initial['hotel'] = selected_hotel
        reservation_form = ReservationForm(initial=initial)

    user_reservations = (
        Reservation.objects.filter(user=request.user)
        .select_related('hotel')
        .order_by('-created_at')
    )

    context = {
        'hotels': hotels,
        'reservation_form': reservation_form,
        'filter_form': filter_form,
        'user_reservations': user_reservations,
    }
    return render(request, 'dashboard/client_portal.html', context)


