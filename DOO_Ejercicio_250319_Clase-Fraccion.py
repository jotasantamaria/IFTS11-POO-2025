"""
Estudiante: Julia de Santa María
Consigna: crear una clase fracción en python, Fraccion que represente dracciones matemáticas. 
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

restricción actual: usar siempre el mismo denominador para simplificar (puede no ser necesario)
el código y no buscar común denominador, ni manualmente ni importando métodos"""

import os
os.system ('clear') #lo sigo usando ;)

class Fraccion:
    def __init__(self, numerador, denominador):
        if denominador == 0:
            print("Error: El denominador no puede ser '0'.")  #revisar función raise ValueError. la encontré en la web. ver cómo imprimir más fácil un mensaje de error.
            SystemExit.exit()  #op para terminar el programa
        self.numerador = numerador
        self.denominador = denominador
    
    def sumar (self , otra_fraccion): #en el numerador se suma la multiplicación cruzada en el denominador se multiplica lineal {a/b + c/d} = (a*d + b*c) / b*d
       nuevo_numerador = (self.numerador * otra_fraccion.denominador)+(self.denominador * otra_fraccion.numerador)
       nuevo_denominador = self.denominador * otra_fraccion.denominador
       return Fraccion (nuevo_numerador , nuevo_denominador)
        
    
    def restar (self , otra_fraccion): #en el numerador se resta la multiplicación cruzada en el denominador se multiplica lineal {a/b - c/d} = (a*d - b*c) / b*d
       nuevo_numerador = (self.numerador * otra_fraccion.denominador)-(self.denominador * otra_fraccion.numerador)
       nuevo_denominador = self.denominador * otra_fraccion.denominador
       return Fraccion (nuevo_numerador , nuevo_denominador)
      
    
    def  multiplicar (self , otra_fraccion): #se multiplica numerador por numerador y denominador por denominador {a/b - c/d} = a*c / c*d
       nuevo_numerador = (self.numerador * otra_fraccion.numerador)
       nuevo_denominador = self.denominador * otra_fraccion.denominador
       return Fraccion (nuevo_numerador , nuevo_denominador)
       
     
    def dividir(self, otra_fraccion): #para el numerador y denominador se multiplica cruzado {a/b - c/d} = (a*d / b*c) 
        if otra_fraccion.numerador == 0:
            print("Error: No se puede dividir por una fracción con numerador cero.")
            sys.exit()
        nuevo_numerador = self.numerador * otra_fraccion.denominador
        nuevo_denominador = self.denominador * otra_fraccion.numerador
        return Fraccion(nuevo_numerador, nuevo_denominador)
       
    
    def mostrar (self):
        if self.denominador == 1:
            return f"{self.numerador}"
        else:
            return f"{self.numerador}/{self.denominador}"

f1 = Fraccion(1, 2)
f2 = Fraccion(3, 4)

suma = f1.sumar(f2)
resta = f2.restar(f1)
multiplica = f1.multiplicar(f2)
divide = f2.dividir(f1)

print(f"El resultado de la suma {f1} más {f2} es: {suma.mostrar()}")
print(f"El resultado de la resta {f2} menos {f1} es: {resta.mostrar()}")
print(f"El resultado de la multiplicación {f1} por {f2} es: {multiplica.mostrar()}")
print(f"El resultado de la dicisión de {f1} en {f2} es: {divide.mostrar()}")

# notas: 
# 1) preguntar / buscar qué hace la función isinstance y ver bien cómo aplicarlo para validar si numerador y denominador son enteros  https://www.w3schools.com/python/ref_func_isinstance.asp .
# 2) ver cómo y de qué serviría implementar el __str__ que mostró al final de la clase.
# 3) revisar función raise ValueError.