import datetime
import  datetime as dt
from dataclasses import dataclass
import math
import names
import random
from collections import UserDict, ChainMap
from collections import deque

# EXAMEN A

# EJERCICIO 1
print('PROPIEDADES')
class Circle():
    def __init__(self):
        self._r = None

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, r):
        if r>0:
            self._r = r

    @property
    def perimeter(self):
        return self._r*2*3.14

    @perimeter.setter
    def perimeter(self, new_perimeter):
        self._r = new_perimeter/(2*3.14)

c = Circle()
c.perimeter = 20
print(c.perimeter)
print(c.radius)


# EJERCICIO 2
print('\n\nSOBRECARGA')
@dataclass
class Transaction():
    id: str
    date: dt.date
    items: [float]

    def __lt__(self, other):
        return (sum(self.items) < sum(other.items))

records = [
    Transaction('01', dt.date(2021,1,2), [1.0, 2.0, 3.0]),
    Transaction('02', dt.date(2021, 1, 4), [5.0, 2.0, 3.0]),
    Transaction('03', dt.date(2021, 1, 9), [10.0, 2.0, 3.0]),
]

print(records[0]<records[1])

records_ordenada = sorted(records)
print(records_ordenada)
records_ordenada_lambda = sorted(records, key = lambda x:sum(x.items))
print(records_ordenada_lambda)


# EJERCICIO 3
print("\n\nDECORADORES")
# LA DECORADA
def log_transform(func):
    def inner(x):
        x = math.log2(x)
        return func(x)
    return inner

# LA QUE DECORA = LOG_TRANSFORM
@log_transform
def f(x):
    return x ** 2

print(f(2))
print(f(4))
print(f(8))


# EJERCICIO 4
print("\n\nLIST COMPREHENSION")
class Graduate():
    def __init__(self):
        self.name = names.get_full_name()
        self.gpa  = round(random.uniform(0,5),1)

lista = [Graduate() for i in range(100)]    # lista de 0 a 100, que cada objeto sea Graduate
print(lista)



# EJERCICIO 5
print("\n\nMAP Y FILTER")
alumnos = [('Scott Rodriguez', 4.5), ('William Gray', 4.5), ('Vincent Sanders', 4.7), ('Robert Nerney', 4.7),
           ('Nancy Moore', 4.6), ('Richard Venable', 4.9), ('Christine Ines', 4.6), ('Elsa Gralak', 4.9),
           ('Joy Braithwaite', 5.0), ('Richard Chase', 4.9), ('Lorraine Kunkel', 4.8), ('Rod Delagarza', 4.5),
           ('Erica Roundtree', 4.6), ('Deneen Rich', 4.6)]
#lista = [(Graduate.nombre), (Graduate.gpa)]
aprobados= list(map(lambda n: [(alumnos[0], alumnos[1])], (filter(lambda n: n[1]>=4.8, alumnos))))
print(aprobados)


# EJERCICIO 6
print("\n\nSOBREARGA")
class Cart(UserDict):
    def __init__(self, nombre, art):
        self.nombre = nombre
        self.art = art

    def __sub__(self, other):
        if self.name == other.name:
            self.art = 1



# EJERCICIO 7
print("\n\nITERADORES")
"""
    Iterador CumMean, que se inicialice con una lista y que devuelva una media de movil, 
    empezando por el último valor.
"""
class CumMean:
    def _init_(self, values: deque[float]):
        self.values = values
        self.accum = 0
        self.n = 0

    def _iter_(self):
        return self

    def _next_(self):
        if not self.values:
            raise StopIteration
        self.accum += self.values.popleft()
        self.n += 1
        return self.accum / self.n


for i in CumMean(deque([2, 4, 6, 8])):
    print(i)














cart_1 = Cart(pen=1, pencil=2)
item = 'pen'

total = cart_1 - item

print(total)  # returns {'pencil': 2}
type(total)  # returns <class '_main_.Cart'>