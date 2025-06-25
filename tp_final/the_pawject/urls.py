from django.urls import path
from . import views

app_name = 'the_pawject'

urlpatterns = [
    path('test-api/', views.test_api_key, name='test_api_key'),
    path('crear/', views.crear_usuario, name='crear_usuario'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_usuario, name='perfil'),
    path('buscar/', views.buscar_animales, name='buscar_animales'),
    path('', views.landing, name='landing'),
]
