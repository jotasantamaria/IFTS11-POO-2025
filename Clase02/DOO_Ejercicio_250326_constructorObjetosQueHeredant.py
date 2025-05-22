import os
os.system ('clear') 
# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

# Clase hija 1
class PerroDomestico(Animal):
    def ladrar(self):
        return "¡Guau!"

# Clase hija 2
class GatoCallejero(Animal):
    def maullar(self):
        return "¡Miau!"

class GeneradorDeObjetos:
    def __init__(self, clase_recibida):
        self.clase_para_usar = clase_recibida

    def crear_instancia(self, valor_nombre):
        return self.clase_para_usar(valor_nombre)

# Generamos un perro
generador_perros = GeneradorDeObjetos(PerroDomestico)
perro = generador_perros.crear_instancia("Firulais")
print(perro.nombre)          # Firulais
print(perro.ladrar())        # ¡Guau!

# Generamos un gato
generador_gatos = GeneradorDeObjetos(GatoCallejero)
gato = generador_gatos.crear_instancia("Mishín")
print(gato.nombre)           # Mishín
print(gato.maullar())        # ¡Miau!
