import os
os.system ('clear') # esto es un método de una clase! los métodos viven dentro de los objetos

class MiEntero:
    def __init__(self,valor):
        self.valor = valor 
    def add(self,other):
        suma = self.valor + other.valor #op sintética return MiEntero(self.valor + other.valor)
        return MiEntero(suma)
        
a = MiEntero(2)
b = MiEntero(3)
c = a.add(b)

print(c.valor)