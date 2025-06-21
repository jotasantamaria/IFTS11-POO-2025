from django.db import models
from datetime import date, timedelta

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    localidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)  # <-- Agregado
    preferencias = models.JSONField(default=dict, blank=True)  # Preferencias de adopción
    animales_adoptados = models.ManyToManyField('Animal', blank=True)

    def __str__(self):
        return self.nombre


class Refugio(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=100)
    capacidad = models.IntegerField()
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)

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

    PELAJE_CHOICES = [
        ('corto', 'Corto'),
        ('medio', 'Medio'),
        ('largo', 'Largo'),
        ('rizado', 'Rizado'),
        ('sin_pelo', 'Sin pelo'),
    ]

    COLOR_CHOICES = [
        ('cafe', 'Café'),
        ('rubio', 'Rubio'),
        ('negro', 'Negro'),
        ('tricolor', 'Tricolor'),
        ('blanco', 'Blanco'),
        ('albino', 'Albino'),
        ('gris', 'Gris'),
        ('atigrado', 'Atigrado'),
        ('marron', 'Marrón'),
    ]

    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('en_proceso', 'En proceso de adopción'),
        ('adoptado', 'Adoptado'),
    ]

    ESTADO_SALUD_CHOICES = [
        ('sano', 'Sano'),
        ('en_tratamiento', 'En tratamiento'),
        ('enfermo', 'Enfermo'),
    ]


    ESTADO_MKTG_CHOICES = [
        ('normal', 'Normal'),
        ('nuevo_ingreso', 'Nuevo ingreso'),
        ('larga_estadia', 'Larga estadía'),
        ('destacado', 'Destacado'),
    ]

    ALERGIA_CHOICES = [
        ('ninguna', 'Ninguna'),
        ('al_polen', 'Polen'),
        ('alimentaria', 'Alimentaria'),
        ('picadura', 'Picaduras'),
        ('otro', 'Otro'),
    ]

    TEMPERAMENTO_CHOICES = [
        ('tranquilo', 'Tranquilo'),
        ('activo', 'Activo'),
        ('agresivo', 'Agresivo'),
    ]

    CONDICION_CHOICES = [
        ('ninguna', 'Ninguna'),
        ('displasia', 'Displasia'),
        ('problema_renal', 'Problema renal'),
        ('diabetes', 'Diabetes'),
        ('otro', 'Otro'),
    ]

    especie = models.CharField(max_length=10, choices=ESPECIE_CHOICES)
    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    tamaño = models.CharField(max_length=10, choices=TAMAÑO_CHOICES)
    peso = models.FloatField()  # admite decimales
    estado_salud = models.CharField(max_length=20, choices=ESTADO_SALUD_CHOICES)
    vacunado = models.BooleanField(default=False)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
    estado_mktg = models.CharField(max_length=20, choices=ESTADO_MKTG_CHOICES, default='normal')
    temperamento = models.CharField(max_length=20, choices=TEMPERAMENTO_CHOICES)
    marketing = models.TextField(blank=True)
    pelaje = models.CharField(max_length=20, choices=PELAJE_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=20, choices=COLOR_CHOICES, blank=True, null=True)
    refugio = models.ForeignKey(Refugio, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_ingreso = models.DateField(null=True, blank=True)
    esterilizado = models.BooleanField(default=False)
    desparasitado = models.BooleanField(default=False)
    ultima_visita_vet = models.DateField(null=True, blank=True)
    
    alergia_tipo = models.CharField(max_length=20, choices=ALERGIA_CHOICES, default='ninguna')
    alergias_texto = models.TextField(blank=True)
    
    condicion_cronica_tipo = models.CharField(max_length=20, choices=CONDICION_CHOICES, default='ninguna')
    condiciones_texto = models.TextField(blank=True)

    notas = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.especie})"

    def edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad

    def es_larga_estadia(self):
        if self.fecha_ingreso:
            return (date.today() - self.fecha_ingreso) >= timedelta(days=180)
        return False


class FotoAnimal(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='fotos_animales/')
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Foto de {self.animal.nombre}"


class FotoRefugio(models.Model):
    refugio = models.ForeignKey(Refugio, on_delete=models.CASCADE, related_name='fotos')
    imagen = models.ImageField(upload_to='fotos_refugios/')
    descripcion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Foto del refugio {self.refugio.nombre}"
