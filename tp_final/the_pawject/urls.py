from django.urls import path
from . import views
from .views import test_api_key, crear_usuario

app_name = 'the_pawject'

urlpatterns = [
    path('test-api/', test_api_key, name='test_api_key'),
    path('crear/', crear_usuario, name='crear_usuario'),
    path('buscar/', views.buscar_animales, name='buscar_animales'),
    path('', views.landing, name='landing'),

]
