import os
os.system ('clear')

class Perro:
    def __init__(self, nombre, raza, edad, tamaño, peso, estsdo_salud, vacunado, estado('disponible','reservado','adoptado'), temperamento, id):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado
        self.temperamento = temperamento
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
    
    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"El estado del perro {self.nombre} ha sido cambiado a {self.estado}.")
        print("::::::::::::::::::::::::::::::::::::")

class Usuario:
    def __init__(self, nombre, apellido, dni, email, direccion, correo, id):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.direccion = direccion
        self.correo = correo
        self.id = id
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")
        print(f"Correo: {self.correo}")
        print(f"ID: {self.id}")
        print("::::::::::::::::::::::::::::::::::::")

"""class Perro:
    nombre = nombre
    raza = raza
    edad = edad
    tamaño = tamaño
    peso = peso
    estado_salud = estado_salud
    vacunado = vacunado
    estado = estado
    temperamento = temperamento
    id = id
    def __init__(self, nombre, raza, edad, tamaño, peso, estsdo_salud, vacunado, estado('disponible','reservado','adoptado'), temperamento, id):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado
        self.temperamento = temperamento
        self.id = id"""