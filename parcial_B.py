# PARCIAL B

# EJERCICIO 3
"""
    Cread una clase Circle, que contiene un único atributo protegido _r (radio).
    Se debe instanciar sin ningún parámetro y con _r fijado a None.
    Mediante propiedades, permitir actualizar el radio fijando el area.
    Que se pueda acceder al protegido con una llamada a .radius.
        c = Circle()
        c.area = 4 * pi
        print(c.area)  # returns 4 * pi, 12.566
        print(c.radius)  # returns 2.0
"""
import math
from dataclasses import dataclass

print("EJERCICIO 3:")
from math import pi


class Circle:
    def __init__(self):
        self._radius = None

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        return round(pi * self._radius**2,2)

    @area.setter
    def area(self, area):
        self._radius = math.sqrt(area/pi)

c = Circle()
c.area = 4 * pi
print(c.area)       # returns 4*pi = 12.566
print(c.radius)     # returns 2.0


# EJERCICIO 4
print('\n\nEJERCICIO 4:')
"""
    Cread una clase Transaction mediante el decorador @dataclass con los atributos:
    - id, una cadena, 
    - date,
    - items: un diccionario con llaves que identifican el nombre del producto (A, B, ...) 
    y valores que corresponden a los kg del producto que se está transaccionando.
    Sobrecargard el operador < de manera que la expresión a < b es verdadera 
    si la suma de kg de a es menor que la suma de kg de b.
    Considerad una lista con los siguientes registros:
    records = [
    TransactionD('01', {'A': 1.0, 'B': 2.0, 'C': 3.0}),
    TransactionD('02', {'A': 10.0, 'B': 2.0, 'C': 3.0}),
    TransactionD('03', {'A': 5.0, 'B': 2.0, 'C': 3.0}),
    ]
    Incluid dos expresiones que devuelva la lista ordenada por kg totales:
    1.  usando sorted directamente sobre  la lista.
    2.  usando sorted pero pasándole una función lambda como llave de ordenación
    Vuestra respuesta debe incluir la clase (incluida el método para sobrecargar <) y las dos expresiones.
"""
from dataclasses import dataclass
import datetime as dt

@dataclass
class Transaction:
    id: str
    items: {str : int}     # metes los valores que corresponden al producto
    def __lt__(self, other):
        return sum(self.items.values()) < sum(other.items.values())

records = [
    Transaction('01', {'A': 1.0, 'B': 2.0, 'C': 3.0}),
    Transaction('02', {'A': 10.0, 'B': 2.0, 'C': 3.0}),
    Transaction('03', {'A': 5.0, 'B': 2.0, 'C': 3.0})
]
print(records[0] < records[1])
records_ordenar = sorted(records)




# EJERCICIO 6
print('\n\nEJERCICIO 6:')
"""
    Programad un decorador que opere con funciones de un sólo parámetro (float).
    Decora:
        @log_transform
        def f(x):
            return x**3
    La función decorada debe aplicar el valor absoluto (abs) sobre el argumento.
    s sin decorar:
        f(-2) = -8.0
    s decorada:
        f(-2) = 8.0 
"""
from typing import Callable
# DECORADOR
def absolute_value(func: Callable) -> Callable:
    def inner(x):
        result = round(abs(x), 2)
        return func(result)
    return inner

# FUNCIÓN DECORADA
@absolute_value
def cubo(x: int) -> float:
    return x**3

print(cubo(-2))


# EJERCICIO 7
print('\n\nEJERCICIO 7:')
"""
    Crear un iterador CumSubstract, que se inicialice mediante un valor inicial 
    y una lista que devuelva:
        for i in CumSubstract(20, [8, 6, 4, 2]):
            print(i)
        debe devolver:
            12.0 (es decir 20 -8)
            6.0 (es decir,  20 - 8 - 6)
            2.0 (es decir,  20 - 8 - 6 - 4)
            0.0 (es decir,  20 - 8 - 6 - 4 - 2)
    Considera revertir la lista antes de almacenarla como atributo 
    (el método reverse() invierte el orden "in place")
"""

