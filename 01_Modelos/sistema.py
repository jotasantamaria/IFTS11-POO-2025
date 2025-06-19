import os
os.system('clear') 

class Sistema:
    def __init__(self):
        self.refugios = []
        self.usuarios = []
        self.animales = []
        self.hogares_transito = []

    def agregar_refugio(self, refugio):
        self.refugios.append(refugio)

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def agregar_animal(self, animal):
        # Intentar asignar a refugio con espacio
        refugio_asignado = Refugio.asignar_a_refugio_disponible(animal, self.refugios)
        if refugio_asignado is None:
            # Si no hay refugios disponibles, asignar a hogar de tránsito
            if self.hogares_transito:
                hogar = self.hogares_transito[0]  # revisar si puedo mejorar la lógica después
                hogar.agregar_animal(animal)
                print(f"{animal.nombre} asignado a hogar de tránsito {hogar.nombre}")
            else:
                print(f"No hay refugios ni hogares de tránsito disponibles para {animal.nombre}")
        else:
            print(f"{animal.nombre} asignado al refugio {refugio_asignado.nombre}")
        self.animales.append(animal)

    def agregar_hogar_transito(self, hogar):
        self.hogares_transito.append(hogar)

    def buscar_animales_por_preferencia(self, preferencias):
        resultados = []
        for animal in self.animales:
            if animal.refugio is None and all(
                getattr(animal, clave, None) == valor for clave, valor in preferencias.items()
                if valor is not None
            ):
                resultados.append(animal)
        return resultados

    def registrar_adopcion(self, usuario, animal):
        usuario.adoptar(animal)
        if animal.refugio:
            animal.refugio.remover_animal(animal)
        elif hasattr(animal, 'hogar_transito') and animal.hogar_transito:
            animal.hogar_transito.remover_animal(animal)
        self.animales.remove(animal)
