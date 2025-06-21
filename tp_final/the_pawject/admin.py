from django.contrib import admin
from .models import Refugio, Animal, Usuario, HogarTransito, FotoAnimal, FotoRefugio

class FotoAnimalInline(admin.TabularInline):  
    model = FotoAnimal
    extra = 1  # esto me va a mostrar un formulario vacío adicional para cargar otra imagen

class AnimalAdmin(admin.ModelAdmin):
    inlines = [FotoAnimalInline]
    filter_horizontal = ('vinculados',)  # agrego esto para elegir fácilmente los animales inseparables en admin

class FotoRefugioInline(admin.TabularInline):
    model = FotoRefugio
    extra = 1

class RefugioAdmin(admin.ModelAdmin):
    inlines = [FotoRefugioInline]

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Refugio, RefugioAdmin)
admin.site.register(Usuario)
admin.site.register(HogarTransito)
admin.site.register(FotoRefugio)
