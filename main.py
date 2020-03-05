from CalculadoraSalario import CalculadoraI
from CategoriaA import CategoriaA
from CategoriaE import CategoriaE
from Empleado import Trabajador


def main():
    result: CalculadoraI = CategoriaA(10000, 200)
    persona: Trabajador = Trabajador("Martion", result)
    persona.display()


if __name__ == '__main__':
    main()
