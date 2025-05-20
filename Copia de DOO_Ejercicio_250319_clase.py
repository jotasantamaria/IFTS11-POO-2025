import os
os.system ('clear') # esto es un método de una clase! los métodos viven dentro de los objetos

class Auto:
    def __init__(self,color,marca):
        self.color = color # atributo del objeto autito estamos construyendo el objeto para después pasarle los atributos específicos al invocarlo
        self.marca = marca # atributo del objeto autito

    def definite(self): # esto es un método de la clase "definite"
        print("Soy un", self.marca, "Color", self.color)

autito = Auto("rojo","Toyota")
autito.definite() #acá se está ejecutando el método "definite" del objeto autito, que pertenece a la clase auto

# encapsulamiento, es una de las principales características del paradigma. El objeto y las clases ya vienen definidos están encapsulados
# son en cierto sentido una "caja negra"
# otro concepto clave es el de "constructor" 

