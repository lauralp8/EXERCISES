"""
TEMA 3: CLASES (PROPIEDADES)
    Cread una clase Circle, que contiene su único atributo protegido _r (radio).
    Se debe instanciar sin parámetro, con _r fijado a None.
    Mediante propiedades, permitid que se pueda actualizar el radio protegido fijando el perímetro,
    y que se pueda acceder al radio protegido con una llamada a .radius.
"""

print('EJERCICIO 1: PROPERTIES')
from math import pi
class Circle:
    def __init__(self):     # se debe instanciar sin parámetro
        self._radio = None

    @property               # metemos el atributo protegido
    def radio(self):
        return self._radio

    # como te dice que el radio cambia conforme al perímetro...
    # creamos perímetro
    @property
    def perimetro(self):
        return 2*pi*self._radio # fórmula del perímetro conforme al radio

    # FUNCIÓN A LA QUE VAMOS A LLAMAR (PERÍMETRO, porque es lo que le vamos a pasar)
    @perimetro.setter
    def perimetro(self, perimetro):
        # pasamos el perímetro y devolvemos el radio en función de dicho perímetro
        self._radio = perimetro/(2*pi)

    @radio.setter
    def radio(self,r):
        if r>0:
            self._radio = r

c = Circle()            # creamos objeto tipo Circle
c.perimetro = 14        # asignamos el perímetro (setter)
print('Valor del perímetro:',c.perimetro)   # devuelve el valor del perímetro (property)
print('Valor del radio:',c.radio)           # devolvemos el radio

print("\n\n EJERCICIO 2: SOBRECARGA DE OPERADORES")
"""
    Cread una clase Transaction mediante el decorador @dataclass con los atributos:
    id: una cadena, date: de tipo datetime.date e items, una lista de valores de coma flotante. 
    Esta lista es una lista de cantidades transaccionas, el kg.
    Sobrecargad el operador < 
    de manera que la expresión a<b es verdadera si la suma de kg en a es < a la suma de kg en b
    Lista ordenada: 
    1. usando sorted directamente sobre la lista. 
    2. usando sorted pero como lambda como llave de ordenación.
"""
from dataclasses import dataclass
import datetime as dt

@dataclass          # el @dataclass funciona como init
class Transaction:
    id: str
    date: dt.date
    items: [float]
    def __lt__(self, other):
        return sum(self.items)<sum(other.items)

records = [
    Transaction('01', dt.date(2021,1,2), [1.0, 2.0, 3.0]),
    Transaction('02', dt.date(2021, 1, 4), [5.0, 2.0, 3.0]),
    Transaction('03', dt.date(2021, 1, 9), [10.0, 2.0, 3.0]),
]

print(records[0]<records[1])

# sorted
print(sorted(records))

# sorted en tupla
ordenar = sorted(records, key=lambda Transaction: sum(Transaction.items))
print(ordenar)

print("\n\n EJERCICIO 3: SOBRECARGA")
"""
    Cread una clase Cart, subclase de dict. Representa un carrito en una sección de web,
    con valores = nombre de artículos y valor entero con el nº de artículos. 
    Sobrecargad el operador resta de manera que a un carrito Cart se le puede restar un artículo
    (una cadena, correspondiente a la llaver del diccionario), devolviendo un objeto cart en el que se le ha eliminado 
    el artículo (eliminada la llave). Comprobado que el objeto que resulta de la resta ya no tiene la llave del artículo 
    y que es un objeto Cart.
"""
class Cart(dict):
    nombre_art: str
    num_art: int
    def __lt__(self, other):


print("\n\n EJERCICIO 4: DECORADORES")
"""
    Hay que importar math
    Si queremos hacer el logaritmo en base 2: j =  math.log2(j)
    Decorador que opere con funciones de un sólo parámetro floar que devuelve un float
        @log_transform
        def f(x):
            return x**2
    La función decorada debe realizar una transformación logarítmica en base 2 
    sobre el argumento antes de aplicar la función f.
    Es decir, s la función sin decorar devuelve:
    f(2) = 4.0
    f(4) = 16.0
    f(8) = 64.0
    La función decorada debe calcular f(log(x,2)):
    f(2) = 1.0
    f(4) = 4.0
    f(8) = 9.0
"""
import math
from typing import Callable
# DECORADOR
def log_transform(func: Callable) -> Callable:
    def inner(x):
        log_result = math.log2(x)
        # llamamos a la función de fuera
        return func(log_result)
    return inner            # returneas directamente TODA la función desde fuera

# DECORADA
@log_transform
def f(x):
    return x**2

print('Valores', f(2), f(4), f(8))

print("\n\n EJERCICIO 7: MAP")
"""
    Usando la lista anterior, cread una lista de tuplas 
    (cada tupla formada por nombre y gpa),
    con los estudiantes de nota >= 4,8
    Usad map y filter sobre la lista
"""
# map lo queremos para pasarlo a una tupla
lista = [('Scott Rodriguez', 4.5), ('William Gray', 4.5), ('Vincent Sanders', 4.7), ('Robert Nerney', 4.7),
         ('Nancy Moore', 4.6), ('Richard Venable', 4.9), ('Christine Ines', 4.6), ('Elsa Gralak', 4.9),
         ('Joy Braithwaite', 5.0), ('Richard Chase', 4.9), ('Lorraine Kunkel', 4.8), ('Rod Delagarza', 4.5),
         ('Erica Roundtree', 4.6), ('Deneen Rich', 4.6)]
print('lista\n', lista)
lista_modificada = list(map(lambda x: (x[0], x[1]),filter(lambda l: l[1]>=4.8, lista)))
print('lista modificada\n', lista_modificada)

