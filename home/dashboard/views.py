from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required # Se necesita loguearse para poder ver las demas rutas
def index(request):
    return render(request, 'dashboard/index.html')

@login_required # Se necesita loguearse para poder ver las demas rutas
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required # Se necesita loguearse para poder ver las demas rutas
def product(request):
    return render(request, 'dashboard/product.html')

@login_required # Se necesita loguearse para poder ver las demas rutas
def order(request):
    return render(request, 'dashboard/order.html')


