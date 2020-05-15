

class Coordenadas:

    def __init__(self):
        self.x = x
        self.y = y

    def mover(self, delta_x, delta_y):
        return Coordenadas(self.x + delta_x, self.y + delta_y)

    def distancia(self, otra_coordenada):

        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y
        
        """
            Pitagoras
            la raiz de la diferencia de las coordenadas al cuadrado
            es la distancia
        """
        return (delta_x**2 + delta_y**2)**0.5
