"""crear una clase fracción en python, Fraccion que represente dracciones matemáticas. 
esta clase permitirá realizar operaciones básicas y mostrar los resultados.
definir la clase con dos atributos,
numerador y denominador (diferente de 0)
implemetar métodos para las fracciones:
sumar (otra_fraccion): retrona una nueva fracción con la suma
restar (otra_fraccion): retrona una nueva fracción con la resta
multiplicar (otra_fraccion): retrona una nueva fracción con la multiplicación
dividir (otra_fraccion): retrona una nueva fracción con la división
agregar un método mostrar() que devuelva la dravvión en formato "a/b".
si el numerador es 1 debe mostrar sólo el numerador ("3" en vez de "3/1")

restricción actual: usar siempre el mismo denominador para simplificar 
el código y no buscar común denominador, ni manualmente ni importando métodos"""

import os
os.system ('clear') # esto es un método de una clase! los métodos viven dentro de los objetos
#Definir la clase persona. que como atributos tenga nombre y edad y que como método tenga saludar "hola yo soy "nombre" y tengo "x" años
class Persona:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    def add (self + otra_fraccion):
       return ResSuma(self.valor , otra_fraccion.valor)
    def  resta (self - otra_fraccion):
       return ResResta(self.valor , otra_fraccion.valor)
    def  multiplicacion (self , otra_fraccion):
       return ResMulti(self.valor * otra_fraccion.valor)
    def  division (self , otra_fraccion):
       return ResDiv(self.valor / otra_fraccion.valor)
    def definite(self):
        print ("Hola yo soy", self.nombre, "y tengo", self.edad, "años.") #alternativa  print ("Hola yo soy %sself.nombre%s y tengo %sself.edad%s años.")


carlota = Persona("Carlota","32")
carlota.definite() #acá se está ejecutando el método "definite" del objeto autito, que pertenece a la clase auto


