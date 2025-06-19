class Usuario:
    def __init__(self, nombre, email, localidad, telefono = None, preferencias = None):

        self.nombre = nombre
        self.email = email
        self.localidad = localidad
        self.telefono = telefono
        self.preferencias = preferencias or {} # dict con las preferencias de adopción 
        self.animales_adoptados = []

    def adoptar (self, animal):
        self.animales_adoptados.append(animal)
        print(f"{self.nombre} ha adoptado a {animal.nombre}.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Localidad: {self.localidad}")
        print(f"Teléfono: {self.telefono or 'No informado'}")
        print("Preferencias de adopción: ")
        for clave, valor in self.preferencias.items():
            print(f"  - {clave}: {valor}")
        print("::::::::::::::::::::::::::::::::::::")

    def actualizar_preferencias(self, clave, valor):
        self.preferencias[clave] = valor