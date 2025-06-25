from django import forms
from the_pawject.models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'email', 'localidad', 'telefono', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_direccion',
                'placeholder': 'Ej. Av. Siempreviva 742'
            }),
        }
from django.contrib.auth.forms import AuthenticationForm

class LoginUsuarioForm(AuthenticationForm):
    pass 