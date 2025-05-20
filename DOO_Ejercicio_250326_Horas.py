# crear una clase horas que tenga horas minutos y segundos. pedir al usuario que ingrese dos horas en formato hh:mm:ss
# crear una función que sume las horas
# crear una función que reste las horas
# crear una función que muestre los resultados

import os
os.system ('clear')

class Horas:
    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def sumar (self,hora2):
        segundos = self.segundos + hora2.segundos
        minutos = self.minutos + hora2.minutos
        horas = self.horas + hora2.horas

        if segundos >= 60:
            minutos += segundos // 60 # acá le sumo el resultado entero de la división para asegurarme trasladar el/los minutos
            segundos = segundos % 60 # uso el módulo para quedarme con el resto en los segundos
        if minutos >= 60:
            horas += minutos // 60 # acá lo mismo que con los segundos, sumo las horas que resulten enteras
            horas += 1 
        if horas >24: 
            horas = horas % 24 # uso el módulo para quedarme con el resto de las horas y que xej: 23 + 2 = 01h

        return Horas(horas, minutos, segundos)
    
    def restar(self, hora2):
        total1 = hora1.horas * 3600 + hora1.minutos * 60 + hora1.segundos
        total2 = hora2.horas * 3600 + hora2.minutos * 60 + hora2.segundos

        diferencia = abs(total1 - total2) #uso el abs porque el cálculo es la diferencia entre una hora y otra. si la primera es menor no me sirve que el resultado sea negativo.

        horas = diferencia // 3600
        minutos = (diferencia % 3600) // 60
        segundos = diferencia % 60

        return Horas(horas, minutos, segundos)
    def mostrar (self):
        print (f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}") #:02d devuelve el número en dos dígitos

# armo una función para convertir el string en ints
def crear_hora_desde_texto(texto):
    partes = texto.split(":")
    hh = int(partes[0])
    mm = int(partes[1])
    ss = int(partes[2])
    return Horas(hh, mm, ss)

    
hora1 = input("Ingrese una hora en formato hh:mm:ss ")
hora2 = input("Ingrese una hora en formato hh:mm:ss ")

hora1 = crear_hora_desde_texto(hora1)
hora2= crear_hora_desde_texto(hora2)

suma = hora1.sumar(hora2)
resta = hora1.restar(hora2)

print ("La suma es: ")
suma.mostrar()
resta.mostrar()






        


