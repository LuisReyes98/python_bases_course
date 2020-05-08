import math
<  # -*- coding: utf-8 -*-


class Complejidad_algoritmica:
    def __init__(self, n):
        self.n = n

    def constante(self):
        return 1

    def logaritmica(self):
        return math.log10(self.n)

    def lineal(self):
        return self.n

    def log_lineal(self):
        return self.n * math.log10(self.n)

    def polinomial(self):
        return self.n**2

    def exponencial(self):
        return 2**self.n


def run():
    # n = 10, 100, 1000 , 1000000

    n = int(input("Introduce el valor de n: "))
    bigO = Complejidad_algoritmica(n)

    print("El tiempo de complejidad constante es:", bigO.constante())
    print("El tiempo de complejidad logaritmica es:", bigO.logaritmica())
    print("El tiempo de complejidad lineal es:", bigO.lineal())
    print("El tiempo de complejidad log lineal es:", bigO.log_lineal())
    print("El tiempo de complejidad polinomial es:", bigO.polinomial())
    print("El tiempo de complejidad exponencial es:", bigO.exponencial()) >
