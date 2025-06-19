
from datetime import date
import os
os.system('clear') 


from gato import Gato
from datetime import date

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
