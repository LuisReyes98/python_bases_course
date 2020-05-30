import random
import math as m


def median(X):
    return sum(X) / len(X)


def variance(X):
    mu = median(X)

    acumulador = 0

    for x in X:
        acumulador += (x - mu)**2

    return acumulador / len(X)


def standard_deviation(X):
    return m.sqrt(variance(X))


if __name__ == "__main__":
    X = [random.randint(1, 21) for i in range(20)]

    mu = median(X)
    Var = variance(X)
    sigma = standard_deviation(X)
    print(f'Areglo X: {X}')
    print(f'Media: {mu}')
    print(f'Varianza: {Var}')
    print(f'Desviacion estandar: {sigma}')
