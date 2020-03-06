from CategoriaA import CategoriaA
from CalculadoraSalario import CalculadoraI


class Trabajador():
    def __init__(self, name: str, type: object):
        self.type = type
        self.name = name

    def display(self):
        print(self.name)
        print(self.type.getSalary())
