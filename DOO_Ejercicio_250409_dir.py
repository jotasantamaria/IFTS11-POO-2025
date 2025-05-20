class Perro(object):
    def __init__(self,name):
        self.name = name
    def ladra(self):
       print("Wof!")

champi = Perro("Champi")
champi.ladra()

print(dir(champi))