# cuadro.py
from figura import Figura

class Cuadro(Figura):
    #Constructor
    def __init__(self, cm_ancho, cm_altura):
        super().__init__(cm_ancho, cm_altura)

#Calcular area cuadro 
    def calcular_area(self):
        return self.cm_ancho * self.cm_altura
