import datetime
from math import sqrt
import dataclasses
from datetime import date

# EXAMEN B

# EJERCICIO 1
print("\n\nPROPERTIES")
class Circle():
    def __init__(self):
        self._r = None

    @property
    def radius(self):
        return self._r

    @radius.setter
    def radius(self, radius):
        if radius>0:
            radius = self._r
            return radius

    @property
    def area(self):
        return 3.14*self._r**2

    @area.setter
    def area(self, area):
        self._r = sqrt(area/3.13)

c = Circle()
c.area = 20
print(c.area)
print(c.radius)


# EJERCICIO 2
print("\n\nSOBRECARGA")
@dataclass
class Transaction:
    id: str
    date: datetime.date
    items: list[float]

    def __lt__(self, other: 'Transaction') -> bool:
        return sum(self.items) < sum(other.items)


records = [
    Transaction('01', dt.date(2021,1,2), [1.0, 2.0, 3.0]),
    Transaction('02', dt.date(2021, 1, 4), [5.0, 2.0, 3.0]),
    Transaction('03', dt.date(2021, 1, 9), [10.0, 2.0, 3.0]),
]

sorted(records, key=lambda t: sum(t.items), reverse=True)
sorted(records)
sorted(records, key=lambda t: t.date, reverse=True)


@dataclass
class TransactionD:
    id: str
    items: dict[str: float]

    def __lt__(self, other: 'TransactionD') -> bool:
        return sum(self.items.values()) < sum(other.items.values())


records = [
    TransactionD('01', {'A': 1.0, 'B': 2.0, 'C': 3.0}),
    TransactionD('02', {'A': 10.0, 'B': 2.0, 'C': 3.0}),
    TransactionD('03', {'A': 5.0, 'B': 2.0, 'C': 3.0}),
]

sorted(records, key=lambda t: sum(t.items.values()), reverse=True)
sorted(records, reverse=True)


# EJERCICIO 3
print("\n\nSOBRECARGA")
"""
from collections import UserDict, ChainMap


class Cart(UserDict):

    def __add__(self, other: 'Cart') -> ChainMap:
        return ChainMap(self, other)


cart_1 = Cart(pen=1, pencil=2)
cart_2 = Cart(rubber=2, paper=8)

total = cart_1 + cart_2

print(total['pencil'])
"""


# EJERCICIO 4
print("\n\nCALLABLE")
from math import log


def log_transform(func: callable) -> callable:
    def g(x: float) -> float:
        return func(log(x, 2))
    return g


@log_transform
def f(x):
    return x ** 2


f(2)  # 1.0
f(4)  # 4.0
f(8)  # 9.0


def absolute(func: callable) -> callable:
    def g(x: float) -> float:
        return func(abs(x))
    return g


@absolute
def f(x):
    return x ** 3


f(2)  # 8.0
f(-2)  # 8.0



