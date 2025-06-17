import os
os.system('clear')

class Perro:
    def __init__(self, nombre, raza, edad, tamaño, peso, estado_salud, vacunado, estado, temperamento, marketing, id):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado  # debería ser un string: 'disponible', 'reservado', 'no disponible'.
        self.temperamento = temperamento
        self.marketing = marketing # debería ser un string: 'nuevo ingreso'
        self.id = id
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso}")
        print(f"Estado de salud: {self.estado_salud}")
        print(f"Vacunado: {'Sí' if self.vacunado else 'No'}")
        print(f"Estado: {self.estado}")
        print(f"Temperamento: {self.temperamento}")
        print(f"ID: {self.id}")
        print("::::::::::::::::::::::::::::::::::::")
    
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
        print(f"El nombre del perro {self.nombre} ha sido cambiado a {self.nombre}.")
        print("::::::::::::::::::::::::::::::::::::")

    def cambiar_raza(self, nueva_raza):
        self.raza = nueva_raza
        print(f"La raza del perro ha sido cambiada a {self.raza}.")
        print("::::::::::::::::::::::::::::::::::::")
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"El estado del perro {self.nombre} ha sido cambiado a {self.estado}.")
        print("::::::::::::::::::::::::::::::::::::")
    
     