import os
os.system ('clear') 

class Perro (object):
    patas = 4
    def __init__(self,nombre,raza):
        self.nombre = nombre
        self.raza = raza
    def habla(self):
        print ("Guau!")
    
class Gato (object):
    patas = 4
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    def habla (self):
        print ("Miau!")
    
#b = Perro ("Champs","Porteño")
#b.habla = "Wow!"
#print(b.habla)

a = [Perro("César","Rope"), Gato("Fuga","Americano"), Perro("Champ","Porteño")]
i=0
while i < len(a):
    a[i].habla()
    i +=1


