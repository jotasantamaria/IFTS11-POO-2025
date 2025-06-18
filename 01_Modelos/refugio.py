from datetime import date
import os
os.system('clear') 

class Refugio:
    def __init__(self, nombre, direccion, localidad, capacidad):
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.capacidad = capacidad  # Cantidad máxima de animales
        self.animales = []  # Lista de animales actualmente en el refugio

    def plazas_disponibles(self):
        return self.capacidad - len(self.animales)

    def agregar_animal(self, animal):
        if self.plazas_disponibles() > 0:
            self.animales.append(animal)
            animal.refugio = self  # Se vincula el animal con este refugio
            print(f"{animal.nombre} fue agregado/a al refugio {self.nombre}.")
        else:
            print(f"No hay plazas disponibles en el refugio {self.nombre}.")

    def remover_animal(self, animal):
        if animal in self.animales:
            self.animales.remove(animal)
            animal.refugio = None
            print(f"{animal.nombre} fue removido/a del refugio {self.nombre}.")
        else:
            print(f"{animal.nombre} no se encuentra en este refugio.")

    def listar_animales(self):
        if not self.animales:
            print(f"El refugio {self.nombre} no tiene animales actualmente.")
        else:
            print(f"Animales en el refugio {self.nombre}:")
            for a in self.animales:
                print(f"- {a.nombre} ({a.especie}, {a.edad} años, {a.tamaño})")
