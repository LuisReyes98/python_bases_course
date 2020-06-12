import random as rand
from bokeh.plotting import figure, show
import matplotlib.pyplot as plt
import numpy as np


def generate_random_matrix(size=20):
    """ Generarar matriz de coordenadas aleatorias """
    matrix = [[rand.randint(0, 30), rand.randint(0, 30)] for _ in range(size)]

    return matrix


def plot_matrix_bokeh(matrix):
    # Generating a graph of the vectors with bokeh
    x_points = []
    y_points = []

    for i in range(len(matrix)):
        x_points.append(matrix[i][0])
        y_points.append(matrix[i][1])

    p = figure(plot_width=400, plot_height=400)

    # add a circle renderer with a size, color, and alpha
    p.circle(x_points, y_points, size=20, color="navy", alpha=0.5)

    # show the results
    show(p)


def plot_matrix_matplot(matrix):
    X = np.array(matrix)

    labels = range(1, len(matrix))
    plt.figure(figsize=(10, 7))
    plt.subplots_adjust(bottom=0.1)
    plt.scatter(X[:, 0], X[:, 1], label='True Position')

    for label, x, y in zip(labels, X[:, 0], X[:, 1]):
        plt.annotate(
            label,
            xy=(x, y), xytext=(-3, 3),
            textcoords='offset points', ha='right', va='bottom')
    plt.show()


if __name__ == "__main__":
    pass

    res = generate_random_matrix()

    # plot_matrix_bokeh(res)
    # plot_matrix_matplot(res)

    print(res)
