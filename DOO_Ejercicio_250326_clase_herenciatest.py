import os
os.system ('clear') 

class Mascota:
    def __init__(self, nombre, edad,raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza

class Perro(Mascota):
    def ladrar (self):
        return "wow!"
    
class Gato(Mascota):
    def maullar (self):
        return "mew!"
    

champ = Perro("Champagne","3","Desconocido")
fuga = Gato("Fuga", "13", "Black coffee")

print(champ.nombre,fuga.nombre)
print(champ.__dict__,fuga.__dict__)

print(champ.ladrar()) 
print(fuga.maullar())
