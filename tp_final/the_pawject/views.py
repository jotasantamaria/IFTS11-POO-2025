from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from django.http import JsonResponse
from .forms.usuario_form import PreferenciasUsuarioForm
from the_pawject.models import PreferenciasUsuario



from .models import Refugio, Animal
from .forms.usuario_form import UsuarioForm, LoginUsuarioForm, RegistroUsuarioForm

def landing(request):
    fotos_refugios = []
    for refugio in Refugio.objects.all()[:5]:
        if refugio.fotos.exists():
            fotos_refugios.append(refugio.fotos.first().imagen.url)

    fotos_animales = []
    for animal in Animal.objects.all()[:5]:
        if animal.fotos.exists():
            fotos_animales.append(animal.fotos.first().imagen.url)

    filtros = {
        'refugio': request.GET.get('refugio', ''),
        'especie': request.GET.get('especie', ''),
        'tamano': request.GET.get('tamano', ''),
    }

    animales = Animal.objects.all()

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
            form = UsuarioForm()
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
            messages.success(request, "Usuario registrado exitosamente.")
            return redirect('the_pawject:perfil')
        else:
            messages.error(request, "Por favor corregí los errores en el formulario.")
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginUsuarioForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect('the_pawject:perfil')
        else:
            messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = LoginUsuarioForm()
    return render(request, 'login.html', {'form': form})


@login_required
def perfil_usuario(request):
    user = request.user
    especies = Animal.ESPECIE_CHOICES
    tamaños = Animal.TAMAÑO_CHOICES
    sexos = Animal.SEXO_CHOICES

    try:
        preferencias = PreferenciasUsuario.objects.get(usuario=user)
    except PreferenciasUsuario.DoesNotExist:
        preferencias = PreferenciasUsuario(usuario=user)
    
    if request.method == 'POST':
        form = PreferenciasUsuarioForm(request.POST, instance=preferencias)
        if form.is_valid():
            form.save()
            messages.success(request, "Preferencias guardadas correctamente.")
            return redirect('the_pawject:perfil')
        else:
            messages.error(request, "Error al guardar las preferencias.")
    else:
        form = PreferenciasUsuarioForm(instance=preferencias)

    context = {
        'user': user,
        'form': form,
        'especies': especies,
        'tamaños': tamaños,
        'sexos': sexos,
    }
    return render(request, 'perfil.html', context)


def logout_view(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente.")
    return redirect('the_pawject:landing')


def test_api_key(request):
    return JsonResponse({"GOOGLE_MAPS_API_KEY": settings.GOOGLE_MAPS_API_KEY or "No definido"})


def buscar_animales(request):
    refugios = Refugio.objects.all()
    animales = Animal.objects.filter(estado='disponible')

    refugio_id = request.GET.get('refugio')
    especie = request.GET.get('especie')
    tamano = request.GET.get('tamano')
    sexo = request.GET.get('sexo')

    if refugio_id:
        animales = animales.filter(refugio_id=refugio_id)
    if especie:
        animales = animales.filter(especie=especie)
    if tamano:
        animales = animales.filter(tamaño=tamano)
    if sexo:
        animales = animales.filter(sexo=sexo)

    context = {
        'refugios': refugios,
        'animales': animales,
        'filtros': {
            'refugio': refugio_id or '',
            'especie': especie or '',
            'tamano': tamano or '',
            'sexo': sexo or '',
        }
    }
    return render(request, 'buscar_animales.html', context)


