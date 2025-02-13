from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notificacion
from .forms import NotificacionForm

# Create your views here.

@login_required
def list_notificaciones(request):
    notificaciones = Notificacion.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'notificaciones/list_notificaciones.html', {'notificaciones': notificaciones})

@login_required
def create_notificacion(request):
    if request.method == 'POST':
        form = NotificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_notificaciones')
    else:
        form = NotificacionForm()
    return render(request, 'notificaciones/create_notificacion.html', {'form': form})

@login_required
def update_notificacion(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    if request.method == 'POST':
        form = NotificacionForm(request.POST, instance=notificacion)
        if form.is_valid():
            form.save()
            return redirect('list_notificaciones')
    else:
        form = NotificacionForm(instance=notificacion)
    return render(request, 'notificaciones/update_notificacion.html', {'form': form})

@login_required
def delete_notificacion(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    if request.method == 'POST':
        notificacion.delete()
        return redirect('list_notificaciones')
    return render(request, 'notificaciones/delete_notificacion.html', {'notificacion': notificacion})

@login_required
def marcar_como_leido(request, pk):
    notificacion = get_object_or_404(Notificacion, pk=pk)
    notificacion.leido = True
    notificacion.save()
    return redirect('list_notificaciones')



