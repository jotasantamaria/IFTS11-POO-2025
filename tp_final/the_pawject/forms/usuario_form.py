from django import forms
from the_pawject.models import Usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

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

class RegistroUsuarioForm(UserCreationForm):
    nombre = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    localidad = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefono = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'id_direccion',
        'placeholder': 'Ej. Av. Siempreviva 742'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nombre', 'localidad', 'telefono', 'direccion']

    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            Usuario.objects.create(
                nombre=self.cleaned_data['nombre'],
                email=self.cleaned_data['email'],
                localidad=self.cleaned_data['localidad'],
                telefono=self.cleaned_data['telefono'],
                direccion=self.cleaned_data['direccion'],
            )
        return user

from the_pawject.models import PreferenciasUsuario

class PreferenciasUsuarioForm(forms.ModelForm):
    class Meta:
        model = PreferenciasUsuario
        fields = ['especie', 'tamano', 'sexo']
        widgets = {
            'especie': forms.Select(attrs={'class': 'form-control'}),
            'tamano': forms.Select(attrs={'class': 'form-control'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }

class LoginUsuarioForm(AuthenticationForm):
    pass

