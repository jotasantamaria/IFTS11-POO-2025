import os 
os.system('clear')

class Coche:
    def __init__(self, color, aceleracion):
        # Atributos de instancia
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0  # Se inicializa en 0

    def __str__(self):
        # Método especial para representar el objeto como string
        return f"Coche(color={self.color}, aceleracion={self.aceleracion}, velocidad={self.velocidad})"

# Crear una instancia de la clase
coche1 = Coche("Rojo", 20)

# Mostrar información del objeto
print(coche1)
