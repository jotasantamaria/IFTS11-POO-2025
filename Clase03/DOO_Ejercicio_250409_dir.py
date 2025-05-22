import os
os.system ('clear')

class HambreException(Exception):
    def __init__(self,mesagge):
        self.mesagge = mesagge
        super().__init__(mesagge)

class Perro(object):
    def __init__(self,name):
        self.name = name
    def ladra(self):
       print("Wof!")

champi = Perro("Champi")
champi.ladra()

print(dir(champi))
print("::::::::::::::::::::::::::::::::::::")
print(champi.__dict__)
print("::::::::::::::::::::::::::::::::::::")
print(dir(object))
print("::::::::::::::::::::::::::::::::::::")
print(dir(Exception))
print("::::::::::::::::::::::::::::::::::::")
print(dir(HambreException))

class Motor(object):
    def encender(self):
        return "El motor está encendido"
    
class Coche (object):
    def __init__(self, marca):
        self.marca = marca
        self.motor = Motor() #composición el coche tiene un motor, le voy a pasar por parámetro el motor

    def encender_coche(self):
        return f"{self.marca}: {self.motor.encender()}"
    
#el coche tiene un motor
coche = Coche ("Toyota")
print(coche.encender_coche())
