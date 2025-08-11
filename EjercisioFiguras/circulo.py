# circulo.py
from figura import Figura
import math

class Circulo(Figura):
    def __init__(self, perimetro, radio):
        super().__init__(perimetro, radio)  # Heredamos como cm_ancho=perímetro, cm_altura=radio
        self.perimetro = perimetro
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)
