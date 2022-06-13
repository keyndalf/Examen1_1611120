# Estudiante: Keyber Yosnar Sequera Avendaño
# Carnet: 16-11120

# Problema 4: Sobrecarga de operadores

# NOTA: Se sustituye el operador unario & (valor absoluto)
#       por el operador abs().

import math

class Cuaternion:
    # Creamos el constructor del cuaternión:
    def __init__(self, a = 0, b = 0, c = 0, d = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    # Sobrecargamos el operador de suma:
    def __add__(self, elemento):
        valorRetorno = Cuaternion(self.a, self.b, self.c, self.d)
        if (type(elemento) == type(Cuaternion())):
            valorRetorno.a += elemento.a
            valorRetorno.b += elemento.b
            valorRetorno.c += elemento.c
            valorRetorno.d += elemento.d
        elif (type(elemento) == type(1.0)):
            valorRetorno.a += elemento
        elif (type(elemento) == type(1)):
            valorRetorno.a += elemento
        else:
            print("Error, está tratando de sumar un cuaternión con un elemento no válido.")
        return valorRetorno
    
    # Sobrecargamos el operador de producto:
    def __mul__(self, elemento):
        valorRetorno = Cuaternion(self.a, self.b, self.c, self.d)
        if (type(elemento) == type(Cuaternion())):
            valorRetorno.a = (self.a * elemento.a) - (self.b * elemento.b) - (self.c * elemento.c) - (self.d * elemento.d)
            valorRetorno.b = (self.a * elemento.b) + (self.b * elemento.a) + (self.c * elemento.d) - (self.d * elemento.c)
            valorRetorno.c = (self.a * elemento.c) - (self.b * elemento.d) + (self.c * elemento.a) + (self.d * elemento.b)
            valorRetorno.d = (self.a * elemento.d) + (self.b * elemento.c) - (self.c * elemento.b) + (self.d * elemento.a)
        elif (type(elemento) == type(1.0)):
            valorRetorno.a *= elemento
        elif (type(elemento) == type(1)):
            valorRetorno.a *= elemento
        else:
            print("Error, está tratando de multiplicar un cuaternión con un elemento no válido.")
        return valorRetorno
    
    # Creamos el operador conjugada:
    def __invert__(self):
        valorRetorno = Cuaternion(self.a, self.b, self.c, self.d)
        valorRetorno.b = -self.b
        valorRetorno.c = -self.c
        valorRetorno.d = -self.d
        return valorRetorno
    
    # Creamos el operador valor absoluto:
    def __abs__(self):
        valorRetorno = math.sqrt((self.a)**2 + (self.b)**2 + (self.c)**2 + (self.d)**2)
        return valorRetorno
    
    # Creamos una representación en string del objeto:
    def __str__(self):
        return f"{self.a} + {self.b}i + {self.c}j + {self.d}k"