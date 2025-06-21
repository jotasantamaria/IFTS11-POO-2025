from django import forms
from the_pawject.models import Refugio

class RefugioForm(forms.ModelForm):
    class Meta:
        model = Refugio
        fields = ['nombre', 'direccion', 'localidad', 'capacidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'id_direccion',  # útil para autocompletado con Google Maps
                'placeholder': 'Ej. Av. Siempreviva 742'
            }),
            'localidad': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad': forms.NumberInput(attrs={'class': 'form-control'}),
        }
