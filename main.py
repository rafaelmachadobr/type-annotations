from collections.abc import Callable
from typing import TypeVar

# Anotações básicas em variáveis

uma_string: str = 'Um valor'
um_inteiro: int = 123456
um_float: float = 1.23
um_boolean: bool = True
um_set: set = {1, 2, 3}  # mais sobre a seguir
uma_lista: list = []  # mais sobre a seguir
um_dicionário: dict = {}  # mais sobre a seguir


# Parâmetros de funções e métodos

def soma(x: int, y: int, z: float) -> float:
    return x + y + z


# Listas

lista_inteiros: list[int] = [1, 2, 3, 4]
lista_strings: list[str] = ["a", "b", "c", "d"]
lista_tuplas: list[tuple] = [(1, "a"), (2, "b")]
lista_listas_int: list[list[int]] = [[1], [4, 5]]

# Dicionários

um_dict: dict[str, int] = {
    "A": 0,
    "B": 0,
    "C": 0,
}

um_dict_de_listas: dict[str, list[int]] = {
    "A": [1, 2],
    "B": [3, 4],
    "C": [5, 6],
}

# Conjuntos (Sets)

um_set_de_inteiros: set[int] = {1, 2, 3}

# Type aliases

ListaInteiros = list[int]
DictListaInteiros = dict[str, ListaInteiros]

um_dict_de_listas_type_aliases: DictListaInteiros = {
    "A": [1, 2],
    "B": [3, 4],
    "C": [5, 6],
}

# Union types

string_e_inteiros: str | int = 1  # Union
string_e_inteiros = "A"  # Sem erros
string_e_inteiros = 2  # Sem erros


# Tipos opcionais

def divisao(x: float, y: float | None = None) -> float:
    if isinstance(y, int | float):
        return x / y
    return x / x


# Callable

SubInteiros = Callable[[int, int], int]


def executa(func: SubInteiros, a: int, b: int) -> int:
    return func(a, b)


def subtracao(a: int, b: int) -> int:
    return a - b


executa(subtracao, 1, 2)

# TypeVar

T = TypeVar('T')


def get_item(list: list[T], index: int) -> T:
    return list[index]


list_int = get_item([1, 2, 3], 1)  # int
list_str = get_item(['a', 'b', 'c'], 1)  # str

# Suas classes também são tipos


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"


def say_my_name(person: Person) -> str:
    return person.full_name


print(say_my_name(Person("John", "Marston")))
