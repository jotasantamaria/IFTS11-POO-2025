import os
os.system ('clear')

"""horas = total // 3600
minutos = (total % 3600) // 60
segundos = total % 60
"""
# // te da las unidades completas (horas, minutos).
# % te da el resto que no alcanzó para formar una hora o un minuto.

#Crear una clase Tiempo que:
#Reciba un número de segundos.
#Tenga un método para convertirlo a horas, minutos y segundos.
#Tenga un método para mostrar el resultado en formato hh:mm:ss.

total_segundos = 7384

class Tiempo:
    def __init__(self, total_segundos):
        self.total_segundos = total_segundos
        self.convertir()
    
    def convertir(self):
        self.horas = self.total_segundos // 3600
        self.minutos = (self.total_segundos % 3600) // 60
        self.segundos = self.total_segundos % 60
    
    def mostrar (self):
        print (f"{self.horas:02d}:{self.minutos:02d}:{self.segundos:02d}") #:02d devuelve el número en dos dígitos
    

hora = int(input("Ingrese la cantidad de segundos: "))
hora = Tiempo(hora)
hora.mostrar()

