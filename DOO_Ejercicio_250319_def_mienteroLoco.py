import os
os.system ('clear') # esto es un método de una clase! los métodos viven dentro de los objetos

class MiEnteroLoco:
    def __init__(self,valor):
        self.valor = valor 
    def add(self,other): #en esta línea se redefine la función "+" en la operación de los nuevos enteros creados y al usar el .add phyton levanta lo que tiene definido como "+"
        suma = self.valor - other.valor # en esa op el método de add resta en lugar de sumar sintética return MiEntero(self.valor - other.valor)
        return MiEnteroLoco(suma)
    def __str__(self):
        return "%d" % self.valor

a = MiEnteroLoco(2)
b = MiEnteroLoco(3)
c = a.add(b) # c = a + b acá sumar equivale a escribir la función "def add(self,other):" 

print(c.valor)