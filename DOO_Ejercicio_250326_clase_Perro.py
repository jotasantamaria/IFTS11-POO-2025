import os
os.system ('clear') 
class Perro(object):
    patas = 4  # atributo de clase

    def __init__(self, nombre, raza):
        self.nombre = nombre  # atributo de instancia
        self.raza = raza      # atributo de instancia
        self.edad = "1 día"   # atributo de instancia

# Creamos el primer perro
a = Perro("César", "Nadie_sabe")
print(a.nombre, a.raza, a.edad, a.patas)  
# → César Nadie_sabe 1 día 4

# Creamos otro perro
b = Perro("Pepito", "Caniche")
b.patas = 21  # Estamos creando un nuevo atributo de instancia en b que oculta el de clase
print(b.nombre, b.raza, b.edad, b.patas)  
# → Pepito Caniche 1 día 21

b.edad = "2 años"  # cambiamos el atributo de instancia 'edad' en b
print(a.nombre, a.raza, a.edad, a.patas)  
# → César Nadie_sabe 1 día 4 (a no se ve afectado)

b.edad = "4 años"
b.patas = 4  # volvemos a darle a b.patas el mismo valor que el de la clase
print(b.nombre, b.raza, b.edad, b.patas)
# → Pepito Caniche 4 años 4
