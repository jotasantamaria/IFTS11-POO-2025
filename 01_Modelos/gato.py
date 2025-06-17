from datetime import date
import os
os.system('clear') 

class Gato:
    def __init__(
        self, nombre, raza, fecha_nacimiento, tamaño, peso, estado_salud, vacunado, estado,
        temperamento, marketing, id, color=None, pelaje=None, foto=None,
        refugio=None, fecha_ingreso=None,
        esterilizado=False, desparasitado=False, ultima_visita_vet=None,
        alergias=None, condiciones_cronicas=None, notas=None
    ):
        self.nombre = nombre
        self.raza = raza
        self.fecha_nacimiento = fecha_nacimiento
        self.tamaño = tamaño
        self.peso = peso
        self.estado_salud = estado_salud
        self.vacunado = vacunado
        self.estado = estado
        self.temperamento = temperamento
        self.color = color
        self.pelaje = pelaje
        self.foto = foto
        self.marketing = marketing
        self.id = id

        # Nuevos atributos
        self.refugio = refugio
        self.fecha_ingreso = fecha_ingreso
        self.esterilizado = esterilizado
        self.desparasitado = desparasitado
        self.ultima_visita_vet = ultima_visita_vet
        self.alergias = alergias or []
        self.condiciones_cronicas = condiciones_cronicas or []
        self.notas = notas

    @property
    def edad(self):
        hoy = date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        if (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day):
            edad -= 1
        return edad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso} kg")
        print(f"Estado de salud: {self.estado_salud}")
        print(f"Vacunado: {'Sí' if self.vacunado else 'No'}")
        print(f"Esterilizado: {'Sí' if self.esterilizado else 'No'}")
        print(f"Desparasitado: {'Sí' if self.desparasitado else 'No'}")
        print(f"Última visita veterinaria: {self.ultima_visita_vet or 'No registrada'}")
        print(f"Alergias: {', '.join(self.alergias) if self.alergias else 'Ninguna'}")
        print(f"Condiciones crónicas: {', '.join(self.condiciones_cronicas) if self.condiciones_cronicas else 'Ninguna'}")
        print(f"Estado: {self.estado}")
        print(f"Temperamento: {self.temperamento}")
        print(f"Color: {self.color}")
        print(f"Pelaje: {self.pelaje}")
        print(f"Foto: {self.foto if self.foto else 'Sin foto'}")
        print(f"Marketing: {self.marketing}")
        print(f"Refugio actual: {self.refugio or 'Sin asignar'}")
        print(f"Fecha de ingreso: {self.fecha_ingreso or 'No registrada'}")
        print(f"ID: {self.id}")
        print(f"Notas: {self.notas or 'Sin notas'}")
        print("::::::::::::::::::::::::::::::::::::")
