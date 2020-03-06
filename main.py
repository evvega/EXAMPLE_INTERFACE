from CalculadoraSalario import CalculadoraI
from CategoriaA import CategoriaA
from CategoriaE import CategoriaE
from Empleado import Trabajador


def main():
    result: CalculadoraI = CategoriaE(25000, 8)
    persona: Trabajador = Trabajador("Evelin", result)
    persona.display()

    result: CalculadoraI = CategoriaA(250000, 5000)
    persona: Trabajador = Trabajador("Andres", result)
    persona.display()



if __name__ == '__main__':
    main()
