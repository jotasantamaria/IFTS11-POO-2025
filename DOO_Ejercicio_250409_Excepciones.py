import os
os.system ('clear')

def divide(a,b):
    resultado = None
    try:
        resultado = a/b
    except TypeError:
        print("Ey! Querés dividir peras con manzanas!")
    except ZeroDivisionError:
        print("Ey! Querés dividir por 0!")
    return resultado

a = divide(10, "divisor")
print(a)

a = divide(10, 0)
print(a)

a = divide(10, 2)
print(a)