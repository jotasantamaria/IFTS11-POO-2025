import os
os.system ('clear')

class Libro:
    def __init__(self, titulo, autor, paginas = 100, idioma = "Español"):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.idioma = idioma

def mostrar_info(self):
    print (f"Título: {self.titulo}")
    print (f"Autor: {self.autor}")
    print (f"Páginas: {self.paginas}")
    print (f"Idioma: {self.idioma}")

#crear libros con diferentes combinaciones
libro1 = Libro("El hombre del castillo","Philip K., Dick", 170, "Español")
libro2 = Libro("Diarios de Filmoteca","Fernando Martín, Peña", 385, "Español")
libro3 = Libro("El arte y la ciencia del food pairing","ernard Lahousse y Peter Coucquyt", 388, "Español")

libro1.mostrar_info()
libro2.mostrar_info()
libro3.mostrar_info()
    