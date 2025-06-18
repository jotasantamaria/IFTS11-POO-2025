from datetime import date
import os
os.system('clear') 

from animal import Animal

class Gato(Animal):
    def __init__(self, *args, **kwargs):
        kwargs["especie"] = "gato"
        super().__init__(*args, **kwargs)