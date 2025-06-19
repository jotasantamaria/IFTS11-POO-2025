import os
os.system('clear') 

class HogarTransito:
    def __init__(self, nombre, direccion, localidad, capacidad, contacto=None):
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.capacidad = capacidad  # este es el máximo de animales en tránsito
        self.contacto = contacto
        self.animales = []  # lista de animales alojados en tránsito

    def plazas_disponibles(self):
        return self.capacidad - len(self.animales)

    def agregar_animal(self, animal):
        if self.plazas_disponibles() > 0:
            self.animales.append(animal)
            animal.hogar_transito = self  # asocia el animal a este hogar de tránsito
            print(f"{animal.nombre} fue alojado en el hogar de tránsito {self.nombre}.")
        else:
            print(f"No hay plazas disponibles en el hogar de tránsito {self.nombre}.")

    def remover_animal(self, animal):
        if animal in self.animales:
            self.anim
