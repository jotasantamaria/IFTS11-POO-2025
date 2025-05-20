import os
os.system ('clear') 

class Perro2:
     patas = 4

     def __init__(self,nombre):
        self.nombre = nombre
    
b = Perro2 ("Champs")
print("Antes del del", b.patas)
print("Antes del del y antes del 99", b.__dict__)
b.patas = 99

print("Antes del del después del 99", b.patas)
print("Antes del del después del 99", b.__dict__)
del b.patas
print("Después del del", b.patas)
print("Después  del del", b.__dict__)

