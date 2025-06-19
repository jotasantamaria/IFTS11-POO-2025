from django.db import models
from datetime import date

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    localidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    preferencias = models.JSONField(default=dict, blank=True)  # Para guardar preferencias de adopción
    animales_adoptados = models.ManyToManyField('Animal', blank=True)

    def __str__(self):
        return self.nombre



class Refugio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=100)
    capacidad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class HogarTransito(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    animales = models.ManyToManyField('Animal', blank=True)

    def plazas_disponibles(self):
        return self.capacidad - self.animales.count()

    def __str__(self):
        return self.nombre


class Animal(models.Model):
    ESPECIE_CHOICES = [
        ('perro', 'Perro'),
        ('gato', 'Gato'),
    ]

    TAMAÑO_CHOICES = [
        ('pequeño', 'Pequeño'),
        ('mediano', 'Mediano'),
        ('grande', 'Grande'),
    ]

    especie = models.CharField(max_length=10, choices=ESPECIE_CHOICES)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tamaño = models.CharField(max_length=10, choices=TAMAÑO_CHOICES)
    peso = models.FloatField()
    estado_salud = models.CharField(max_length=100)
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=50)  # Podés usar choices también
    temperamento = models.CharField(max_length=100)
    marketing = models.TextField(blank=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    pelaje = models.CharField(max_length=50, blank=True, null=True)
    foto = models.ImageField(upload_to='fotos_animales/', blank=True, null=True)
    refugio = models.ForeignKey(Refugio, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    esterilizado = models.BooleanField(default=False)
    desparasitado = models.BooleanField(default=False)
    ultima_visita_vet = models.DateField(null=True, blank=True)
    alergias = models.TextField(blank=True)
    condiciones_cronicas = models.TextField(blank=True)
    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

    def edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad