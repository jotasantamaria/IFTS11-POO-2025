from django.urls import path
from .views import test_api_key, crear_usuario

app_name = 'usuarios'  # Namespace para URLs de la app

urlpatterns = [
    path('test-api/', test_api_key, name='test_api_key'),
    path('crear/', crear_usuario, name='crear_usuario'),
]
