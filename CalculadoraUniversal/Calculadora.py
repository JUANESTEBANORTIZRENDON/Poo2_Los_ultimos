"""
Módulo: calculadora.py
Calculadora que opera con números heterogéneos:
1) Convierte ambos a decimal (valor_decimal).
2) Aplica operación (+, -, *, /).
3) Intenta devolver en el tipo del operando izquierdo:
   - Si el tipo NO permite fracciones y el resultado NO es entero -> devuelve Decimal.
Reglas extra para romanos:
- Si el operando izquierdo es romano, SOLO se permite la suma (+).
- El resultado debe estar en 1..100 (I..C) y ser entero; de lo contrario, inválido.
"""

from Decimales import NumeroDecimal
from Binario import NumeroBinario
from Octal import NumeroOctal
from Hexadecimal import NumeroHexadecimal
from Romano import NumeroRomano
from NumeroUniversal import es_entero

class Calculadora:
    def operar(self, num1, num2, operacion):
        # Validaciones base
        if not num1.valido:
            r = NumeroDecimal("0"); r.valido = False
            r.mensaje_error = "Operando izquierdo inválido"
            return r
        if not num2.valido:
            r = NumeroDecimal("0"); r.valido = False
            r.mensaje_error = "Operando derecho inválido"
            return r

        # Regla especial: romano a la izquierda -> solo suma
        if num1.tipo == "rom" and operacion != "+":
            r = NumeroDecimal("0"); r.valido = False
            r.mensaje_error = "Romano: solo se permite la suma (+)"
            return r

        a = num1.valor_decimal
        b = num2.valor_decimal

        # Operación
        if operacion == "+":
            res = a + b
        elif operacion == "-":
            res = a - b
        elif operacion == "*":
            res = a * b
        elif operacion == "/":
            if b == 0:
                r = NumeroDecimal("0"); r.valido = False
                r.mensaje_error = "División por cero"
                return r
            res = a / b
        else:
            r = NumeroDecimal("0"); r.valido = False
            r.mensaje_error = "Operación no soportada"
            return r

        # Devolución por tipo del operando izquierdo
        if num1.tipo == "dec":
            resultado = NumeroDecimal("0"); resultado.valor_decimal = res; return resultado

        elif num1.tipo == "bin":
            if not es_entero(res):
                d = NumeroDecimal("0"); d.valor_decimal = res; return d
            tmp = NumeroBinario("0"); tmp.valor_decimal = res; return tmp

        elif num1.tipo == "oct":
            if not es_entero(res):
                d = NumeroDecimal("0"); d.valor_decimal = res; return d
            tmp = NumeroOctal("0"); tmp.valor_decimal = res; return tmp

        elif num1.tipo == "hex":
            if not es_entero(res):
                d = NumeroDecimal("0"); d.valor_decimal = res; return d
            tmp = NumeroHexadecimal("0"); tmp.valor_decimal = res; return tmp

        elif num1.tipo == "rom":
            # Solo suma, entero y rango 1..100
            if not es_entero(res):
                r = NumeroDecimal("0"); r.valido = False
                r.mensaje_error = "Romano: el resultado no es entero"
                return r
            entero = int(round(res))
            if entero < 1 or entero > 100:
                r = NumeroDecimal("0"); r.valido = False
                r.mensaje_error = "Romano: resultado fuera de rango (I..C)"
                return r
            tmp = NumeroRomano("I")  # placeholder
            tmp.valor_decimal = float(entero)
            return tmp

        # Fallback
        d = NumeroDecimal("0"); d.valor_decimal = res; return d
