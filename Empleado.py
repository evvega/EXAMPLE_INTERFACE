from CategoriaA import CategoriaA
from CalculadoraSalario import CalculadoraI


class Trabajador(CalculadoraI):

    def __init__(self, name: str, type: CalculadoraI):
        self.type = type
        self.name = name

    def display(self, name: str, type: CalculadoraI):
        print(name)
        print(type.getSalary())
