from datetime import date #para cálculo de edad
import os
os.system('clear')

class Perro:
    def __init__(self, nombre, raza, fecha_nacimiento, tamaño, peso, estado_salud, vacunado, estado, temperamento, marketing, id):
        self.nombre = nombre
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado  # debería ser un string: 'disponible', 'reservado', 'no disponible'.
        self.temperamento = temperamento
        self.marketing = marketing # debería ser un string: 'nuevo ingreso'
        self.id = id
    
    
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

    @property #parece un atributo y se llama como a un atributo pero es un código que calcula la edad cada vez
    def edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        print("::::::::::::::::::::::::::::::::::::")

    def cambiar_peso(self, nuevo_peso):
        self.peso = nuevo_peso
        print(f"El estado del perro {self.nombre} ha sido cambiado a {self.peso}.")
        print("::::::::::::::::::::::::::::::::::::")

    def cambiar_estado_salud(self, nuevo_estado_salud):
        self.estado_salud = nuevo_estado_salud
        print(f"El estado del perro {self.nombre} ha sido cambiado a {self.estado_salud}.")
        print("::::::::::::::::::::::::::::::::::::")
    
    def cambiar_temperamento (self, nuevo_temperamento):
        self.temperamento = nuevo_temperamento
        print(f"El temperamento del perro {self.nombre} ha sido cambiado a {self.temperamento}.")
        print("::::::::::::::::::::::::::::::::::::")
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años") #probando que se calcule con la fecha del sistema
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso}")
        print(f"Estado de salud: {self.estado_salud}")
        print(f"Vacunado: {'Sí' if self.vacunado else 'No'}") #esto podría ser un subatributo dependiente de estado_salud, conviene?
        print(f"Estado: {self.estado}")
        print(f"Temperamento: {self.temperamento}")
        print(f"ID: {self.id}")
        print("::::::::::::::::::::::::::::::::::::")