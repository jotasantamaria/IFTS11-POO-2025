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

#para crear los libros primero tengo que crear las variables que pasaré como parámetros en la clase libro para crear cada objeto 
#después aplico el método
#le agregamos un while
lista_libros = []

contTitulos = 0
while contTitulos < 4:

    print (f"\n Ingresá los siguientes datos")

    titulo1 = input("Ingrese el Título")
    autor1 = input("Intrese el autor")
    cantidadPag1= int(input("Ingrese la cantidad de páginas"))
    idioma1 = input("Ingrese el idioma")

    libro1 = Libro(titulo1, autor1, cantidadPag1, idioma1)
    

    contTitulos +=1

    titulo2 = input("Ingrese el Título")
    autor2 = input("Intrese el autor")
    cantidadPag2= int(input("Ingrese la cantidad de páginas"))               
    idioma2 = input("Ingrese el idioma")

    libro2 = Libro(titulo2, autor2, cantidadPag2, idioma2)
   
    contTitulos +=1
    
    titulo3 = input("Ingrese el Título")
    autor3 = input("Intrese el autor")
    cantidadPag3= int(input("Ingrese la cantidad de páginas"))
    idioma3 = input("Ingrese el idioma")

    libro3 = Libro(titulo3, autor3, cantidadPag3, idioma3)

    contTitulos +=1

libro1.mostrar_info()
libro2.mostrar_info()
libro3.mostrar_info()
