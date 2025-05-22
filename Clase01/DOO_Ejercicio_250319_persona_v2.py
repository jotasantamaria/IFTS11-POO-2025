import os
os.system ('clear') # esto es un método de una clase! los métodos viven dentro de los objetos
#Definir la clase persona. que como atributos tenga nombre y edad y que como método tenga saludar "hola yo soy "nombre" y tengo "x" años
class Persona:
    def __init__(self, nombre, edad, peso, altura, direccion):
        self.nombre = nombre
        self.edad = edad
        self.peso = peso 
        self.altura = altura
        self.direccion = direccion    


    def definite(self):
        print ("Hola yo soy", self.nombre, "y tengo", self.edad, "años. Peso", self.peso, "Kg y mido", self.altura, "m. Vivo en", self.direccion, "C.A.B.A" ) #alternativa  print ("Hola yo soy %sself.nombre%s y tengo %sself.edad%s años.")


carlota = Persona("Carlota","32","57","1,75","Gaona 1234")
carlota.definite() #acá se está ejecutando el método "definite" del objeto carlota, que pertenece a la clase persona

print(dir(carlota))
