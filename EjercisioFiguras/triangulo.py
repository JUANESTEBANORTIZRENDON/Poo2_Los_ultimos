# triangulo.py
from figura import Figura

class Triangulo(Figura):
    def __init__(self, cm_ancho, cm_altura):
        super().__init__(cm_ancho, cm_altura)

    def calcular_area(self):
        return (self.cm_ancho * self.cm_altura) / 2
