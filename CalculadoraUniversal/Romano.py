"""
NumeroRomano:
- Rango: 1..100 (I..C)
- En la calculadora: si el operando izquierdo es romano, SOLO suma (+).
"""

from NumeroUniversal import NumeroUniversal

VALOR_ROMANO = {"I":1, "V":5, "X":10, "L":50, "C":100}
MAPA_ENTERO_A_ROMANO = [
    (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
]

class NumeroRomano(NumeroUniversal):
    def __init__(self, literal):
        super().__init__(literal)
        self.tipo = "rom"
        self.permite_fraccion = False
        self.analizar()

    def analizar(self):
        texto = self.literal.strip().upper()
        if len(texto) == 0:
            self.valido = False; self.mensaje_error = "Romano vacío"; return
        for ch in texto:
            if ch not in VALOR_ROMANO:
                self.valido = False; self.mensaje_error = "Carácter romano inválido"; return

        total = 0; i = 0
        while i < len(texto):
            v = VALOR_ROMANO[texto[i]]
            if i + 1 < len(texto):
                v2 = VALOR_ROMANO[texto[i+1]]
                if v < v2:
                    total += (v2 - v); i += 2; continue
            total += v; i += 1

        if total < 1 or total > 100:
            self.valido = False; self.mensaje_error = "Romano fuera de rango (I..C)"; return

        self.valor_decimal = float(total)

    def a_cadena_base_propia(self, valor_decimal):
        if not self.es_entero(valor_decimal):
            return "(no entero)"
        v = self.a_entero(valor_decimal)
        if v < 1 or v > 100:
            return "(fuera de rango)"
        res = ""
        for val, rom in MAPA_ENTERO_A_ROMANO:
            while v >= val:
                res += rom
                v -= val
        return res
