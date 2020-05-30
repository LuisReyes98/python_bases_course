import random
import math as m
from statistics import standard_deviation, median


def throw_needles(number_of_needles):
    inside_circle = 0

    for _ in range(number_of_needles):
        x = random.random() * random.choice([-1, 1])

        y = random.random() * random.choice([-1, 1])

        distance_from_center = m.sqrt(x**2 + y**2)

        if distance_from_center <= 1:
            inside_circle += 1

    return (4 * inside_circle) / number_of_needles


def estimation(number_of_needles, number_of_tries):
    estimations = []

    for _ in range(number_of_tries):
        pi_estimation = throw_needles(number_of_needles)

        estimations.append(pi_estimation)

    median_estimation = median(estimations)

    sigma = standard_deviation(estimations)

    print(f'Est={round(median_estimation, 5)}, sigma={round(sigma, 5)}, agujas={number_of_needles}')

    return (median_estimation, sigma)


def estimate_pi(precision, number_of_tries):
    number_of_needles = 1000
    sigma = precision

    while sigma >= precision / 1.96:  # sigma con 95% de confianza
        median, sigma = estimation(number_of_needles, number_of_tries)
        number_of_needles *= 2

    return median


if __name__ == "__main__":
    """
        Con cada iteracion se logra
        reducir la desviacion estandar
        lo cual genera una respuesta

        estadisticamente valida

        lo que es muy diferente a una respuesta valida

        lo que significa que el valor real se encuentra
        en el rango de la media mas o menos la desviacion estandar

        y con cada iteracion este rango se hace muchisimo mas pequeño

        mas no llegara a dar una respuesta exactamente correcta
    """
    res = estimate_pi(0.01, 1000)
    print(res)
