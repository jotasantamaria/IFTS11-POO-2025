from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import PreferenciasUsuario # sin el punto, busca en la raíz del proyecto o en el path de Python, y eso da error.


class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True, 
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
        })
    )
    first_name = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre',
        })
    )
    last_name = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Apellido',
        })
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña',
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña',
        })


class LoginUsuarioForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
            'autofocus': True,
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
        })
    )


class PreferenciasUsuarioForm(forms.ModelForm):
    class Meta:
        model = PreferenciasUsuario
        fields = ['especie', 'tamano', 'sexo']
        widgets = {
            'especie': forms.Select(choices=[('', 'Cualquier especie'), ('perro', 'Perro'), ('gato', 'Gato')]),
            'tamano': forms.Select(choices=[('', 'Cualquier tamaño'), ('pequeño', 'Pequeño'), ('mediano', 'Mediano'), ('grande', 'Grande')]),
            'sexo': forms.Select(choices=[('', 'Cualquier sexo'), ('macho', 'Macho'), ('hembra', 'Hembra')]),
        }
