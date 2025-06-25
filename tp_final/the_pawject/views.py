from django.conf import settings
from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required
from .forms.usuario_form import UsuarioForm, LoginUsuarioForm
from .models import Refugio, Animal
from django.http import JsonResponse

from django.shortcuts import render
from .models import Refugio, Animal

def landing(request):
    fotos_refugios = []  # para el carrusel
    for refugio in Refugio.objects.all()[:5]:
        if refugio.fotos.exists():
            fotos_refugios.append(refugio.fotos.first().imagen.url)

    return render(request, 'landing.html', {
        'fotos_refugios': fotos_refugios,
    })

    fotos_animales = []
    for animal in Animal.objects.all()[:5]:
        if animal.fotos.exists():
            fotos_animales.append(animal.fotos.first().imagen.url)

   
    animales = Animal.objects.all() #para búsqueda por preferencias
    filtros = {
        'refugio': request.GET.get('refugio', ''),
        'especie': request.GET.get('especie', ''),
        'tamano': request.GET.get('tamano', ''),
    }

    if filtros['refugio']:
        animales = animales.filter(refugio__id=filtros['refugio'])
    if filtros['especie']:
        animales = animales.filter(especie__iexact=filtros['especie'])
    if filtros['tamano']:
        animales = animales.filter(tamaño__iexact=filtros['tamano'])

    refugios = Refugio.objects.all()

    context = {
        'fotos_refugios': fotos_refugios,
        'fotos_animales': fotos_animales,
        'animales': animales,
        'refugios': refugios,
        'filtros': filtros,
    }
    return render(request, 'landing.html', context)


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

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('the_pawject:landing')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginUsuarioForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('the_pawject:landing')
    else:
        form = LoginUsuarioForm()
    return render(request, 'login.html', {'form': form})

@login_required
def perfil_usuario(request):
    return render(request, 'perfil.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('the_pawject:landing')

def test_api_key(request):
    return JsonResponse({"GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY or "No definido"})

def buscar_animales(request):
    refugios = Refugio.objects.all()
    animales = Animal.objects.filter(estado='disponible')  #motrar sólo los disponibles

   
    refugio_id = request.GET.get('refugio')
    especie = request.GET.get('especie')
    tamano = request.GET.get('tamano')

    if refugio_id:
        animales = animales.filter(refugio_id=refugio_id)
    if especie:
        animales = animales.filter(especie=especie)
    if tamano:
        animales = animales.filter(tamaño=tamano)

    context = {
        'refugios': refugios,
        'animales': animales,
        'filtros': {
            'refugio': refugio_id or '',
            'especie': especie or '',
            'tamano': tamano or '',
        }
    }
    return render(request, 'buscar_animales.html', context)