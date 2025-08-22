"""
Calculadora: opera (+, -, *, /) con números heterogéneos.
Hereda de NumeroUniversal para usar self.es_entero(...) sin funciones sueltas.
"""

from Decimales import NumeroDecimal
from Binario import NumeroBinario
from Octal import NumeroOctal
from Hexadecimal import NumeroHexadecimal
from Romano import NumeroRomano
from NumeroUniversal import NumeroUniversal

class Calculadora(NumeroUniversal):
    def __init__(self):
        super().__init__("0")  # sólo para acceder a utilidades de la base

    def operar(self, num1, num2, operacion):
        if not num1.valido:
            r = NumeroDecimal("0"); r.valido = False; r.mensaje_error = "Operando izquierdo inválido"; return r
        if not num2.valido:
            r = NumeroDecimal("0"); r.valido = False; r.mensaje_error = "Operando derecho inválido"; return r

        if num1.tipo == "rom" and operacion != "+":
            r = NumeroDecimal("0"); r.valido = False; r.mensaje_error = "Romano: solo se permite la suma (+)"; return r

        a = num1.valor_decimal; b = num2.valor_decimal

        if operacion == "+":   res = a + b
        elif operacion == "-": res = a - b
        elif operacion == "*": res = a * b
        elif operacion == "/":
            if b == 0:
                r = NumeroDecimal("0"); r.valido = False; r.mensaje_error = "División por cero"; return r
            res = a / b
        else:
            r = NumeroDecimal("0"); r.valido = False; r.mensaje_error = "Operación no soportada"; return r

        # Devolver en el tipo del operando izquierdo, respetando fracciones / rango
        if num1.tipo == "dec":
            resultado = NumeroDecimal("0"); resultado.valor_decimal = res; return resultado

        elif num1.tipo == "bin":
            if not self.es_entero(res):
                d = NumeroDecimal("0"); d.valor_decimal = res; return d
            tmp = NumeroBinario("0"); tmp.valor_decimal = res; return tmp

        elif num1.tipo == "oct":
            if not self.es_entero(res):
                d = NumeroDecimal("0"); d.valor_decimal = res; return d
            tmp = NumeroOctal("0"); tmp.valor_decimal = res; return tmp

        elif num1.tipo == "hex":
            if not self.es_entero(res):
                d = NumeroDecimal("0"); d.valor_decimal = res; return d
            tmp = NumeroHexadecimal("0"); tmp.valor_decimal = res; return tmp

        elif num1.tipo == "rom":
            if not self.es_entero(res):
                r = NumeroDecimal("0"); r.valido = False; r.mensaje_error = "Romano: el resultado no es entero"; return r
            entero = int(round(res))
            if entero < 1 or entero > 100:
                r = NumeroDecimal("0"); r.valido = False; r.mensaje_error = "Romano: resultado fuera de rango (I..C)"; return r
            tmp = NumeroRomano("I"); tmp.valor_decimal = float(entero); return tmp

        d = NumeroDecimal("0"); d.valor_decimal = res; return d
