from CalculadoraSalario import CalculadoraI


class CategoriaA(CalculadoraI):
    def __init__(self, salario_base: float, overtime: float):
        self.salario_base = salario_base
        self.overtime = overtime

    def getSalary(self):
        return self.salario_base + self.overtime
