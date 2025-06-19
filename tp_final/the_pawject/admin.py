from django.contrib import admin
from .models import Refugio, Animal, Usuario, HogarTransito, FotoAnimal

class FotoAnimalInline(admin.TabularInline):  
    model = FotoAnimal
    extra = 1  # esto me va a mostrar un formulario vacío adicional para cargar otra imagen

class AnimalAdmin(admin.ModelAdmin):
    inlines = [FotoAnimalInline]

admin.site.register(Refugio)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Usuario)
admin.site.register(HogarTransito)
