from datetime import date
import os
os.system('clear') 

from animal import Animal

class Perro(Animal):
    def __init__(self, *args, **kwargs):
        kwargs["especie"] = "perro"
        super().__init__(*args, **kwargs)
