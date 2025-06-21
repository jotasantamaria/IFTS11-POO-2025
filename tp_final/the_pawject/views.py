from django.conf import settings
from django.shortcuts import render
from .forms.usuario_form import UsuarioForm
from django.http import JsonResponse

def crear_usuario(request):
    success = False
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = UsuarioForm()  # limpiar formulario para nuevo ingreso
    else:
        form = UsuarioForm()
    
    return render(request, 'usuarios/crear_usuario.html', {
        'form': form,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
        'success': success,
    })

def test_api_key(request):
    return JsonResponse({"GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY or "No definido"})
