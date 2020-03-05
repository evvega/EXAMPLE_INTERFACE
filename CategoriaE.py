from CalculadoraSalario import CalculadoraI


class CategoriaE(CalculadoraI):
    def __init__(self, valor_hora: float, numero_horas: int):
        self.valor_hora = valor_hora
        self.numero_horas = numero_horas

    def getSalary(self, valor_hora: float, numero_horas: int):
        return valor_hora * numero_horas
