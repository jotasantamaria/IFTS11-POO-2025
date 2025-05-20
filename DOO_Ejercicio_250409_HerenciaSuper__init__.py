import os
os.system ('clear')

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak (self):
        return f"{self.name} hace un sonido."

class Perro (Animal):
    def __init__(self,name,breed):
        super().__init__(name) #llama al init de la clase padre
        self.breed = breed
    def speak (self):
        return f"Un {self.name}, un {self.breed}, ladra."
    
perro = Perro("Max","labrador")

print(perro.speak()) #Max, un labrador, ladra.