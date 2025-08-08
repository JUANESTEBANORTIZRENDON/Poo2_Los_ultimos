# main.py para llamar las clases y crear los
from figura import Figura
from cuadro import Cuadro
from triangulo import Triangulo
from circulo import Circulo

# Crear objetos de cada figura
cuadro = Cuadro(5, 5)
triangulo = Triangulo(10, 6)
circulo = Circulo(perimetro=0, radio=4)  # El perímetro no lo usamos aquí para área

# Mostrar resultados
print(f"Área del cuadro: {cuadro.calcular_area()} cm²")
print(f"Área del triángulo: {triangulo.calcular_area()} cm²")
print(f"Área del círculo: {circulo.calcular_area():.2f} cm²")
#modificacio n

