import os
os.system ('clear') # esto es un método de una clase! los métodos viven dentro de los objetos

class Auto:
    def __init__(self,color,marca):
        self.color = color
        self.marca = marca

    def definite(self):
        print("Soy un", self.marca, "Color", self.color)

autito = Auto("rojo","Toyota")
autito.definite()