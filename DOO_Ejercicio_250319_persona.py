import os
os.system ('clear') # esto es un método de una clase! los métodos viven dentro de los objetos
#Definir la clase persona. que como atributos tenga nombre y edad y que como método tenga saludar "hola yo soy "nombre" y tengo "x" años
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def definite(self):
        print ("Hola yo soy", self.nombre, "y tengo", self.edad, "años.")


carlota = Persona("Carlota","32")
carlota.definite() #acá se está ejecutando el método "definite" del objeto autito, que pertenece a la clase auto


