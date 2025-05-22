import os
os.system ('clear')

"""class HambreException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(message)

try:
 raise HambreException("Emiliano")
except HambreException as e:
    print("se quedó sin energía", e)"""


class HambreException(Exception):
    def __init__(self, persona, nivel_de_hambre, ultima_comida):
        self.persona = persona
        self.nivel_de_hambre = nivel_de_hambre
        self.ultima_comida = ultima_comida
        mensaje = f"{persona} tiene hambre nivel {nivel_de_hambre}, última comida a las {ultima_comida}."
        super().__init__(mensaje)

try:
    raise HambreException("Emiliano", 9, "10:30")
except HambreException as e:
    print("💥 Se lanzó una excepción personalizada:")
    print("Mensaje visible con print(e):")
    print(e)
    print("\n📦 Contenido de e.__dict__:")
    print(e.__dict__)

