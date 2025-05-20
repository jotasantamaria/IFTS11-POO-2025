import os
os.system ('clear')

class CustomError(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)#acá llamo a la clase de la que hereda, que es Exception

try:
    raise CustomError("Ocurrió un error personalizado")
except CustomError as e:
    print(e)