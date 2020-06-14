import random as rand
from bokeh.plotting import figure, show
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.cluster.hierarchy import dendrogram, linkage
from matplotlib import pyplot as plt


def generate_random_matrix(size=20):
    """ Generarar matriz de coordenadas aleatorias """
    matrix = [(rand.randint(0, 30), rand.randint(0, 30)) for _ in range(size)]

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


def points_ecludian_distance(pointA, pointB):
    """
        pointA: touple (x,y)
        pointB: touple (x,y)
    """
    return math.sqrt((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)


def hierarchical_cluster_scipy(matrix):
    numpyArray = np.array(matrix)

    linked = linkage(numpyArray, 'single')

    labelList = range(0, len(numpyArray))

    plt.figure(figsize=(10, 7))
    dendrogram(
        linked,
        orientation='top',
        labels=labelList,
        distance_sort='descending',
        show_leaf_counts=True
    )
    plt.show()


def hierarchical_cluster_exercise(matrix, dendrogram):
    """
        Para construir el dendrograma al emepezar cada punto es un cluster,
        con un unico elemento, entonces se calula
        la distancia entre todos los puntos,
        luego los puntos con la distancia mas pequeña se vuelven un cluster,

        ahora se ejecuta todo de nuevo y los cluster con mas de un punto
        abarcan todos sus puntos para comparar
        esto se repite recursivamente hasta que solo queda
        un cluster repartido por jerarquia
    """
    pass

    # smallest_distance = points_ecludian_distance(dendrogram[0], dendrogram[0])
    # for i in range(len(dendrogram)):
    #     for j in range(len(dendrogram) - i):
    #         distance
    # if len(dendrogram) == 1:
    #     return dendrogram
    # else:
    #     return hierarchical_cluster_exercise(matrix, dendrogram)


def kmeans_clustering(parameter_list):
    pass


if __name__ == "__main__":
    coordinates_matrix = generate_random_matrix()

    # plot_matrix_bokeh(coodinates_matrix)
    print(coordinates_matrix)

    exercise = hierarchical_cluster_exercise(
        coordinates_matrix,
        coordinates_matrix
    )
    # plot_matrix_matplot(coodinates_matrix)

    # hierarchical_cluster_scipy(coodinates_matrix)
