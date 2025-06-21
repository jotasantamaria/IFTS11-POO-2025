
from datetime import date
import os
os.system('clear') 

from datetime import date
from sistema import Sistema 
from refugio import Refugio
from hogar_transito import HogarTransito
from usuario import Usuario
from perro import Perro
from gato import Gato


gato = Gato(
    nombre="Fuga",
    raza="Americano pelo corto",
    fecha_nacimiento=date(2010, 10, 9),
    tamaño="pequeño",
    peso=5.5,
    estado_salud="Bueno",
    vacunado=True,
    estado="En adopción",
    temperamento="Tranquilo",
    marketing="Ideal para vivir en depto",
    id="G001",
    color="Negro",
    pelaje="Corto"
)

gato.mostrar_info()
