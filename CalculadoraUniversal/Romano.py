"""
NumeroRomano:
- Entrada y salida en números romanos (I, V, X, L, C) → rango 1..100.
- En la calculadora: si el operando izquierdo es romano, SOLO se permite la suma.
- El resultado debe quedar en 1..100; si no, se marca inválido.
"""

from NumeroUniversal import NumeroUniversal, es_entero, a_entero

# Diccionario romano → decimal (hasta C)
VALOR_ROMANO = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
}

# Mapa ordenado (entero → romano) con notación sustractiva hasta C
MAPA_ENTERO_A_ROMANO = [
    (100, "C"),
    (90,  "XC"),
    (50,  "L"),
    (40,  "XL"),
    (10,  "X"),
    (9,   "IX"),
    (5,   "V"),
    (4,   "IV"),
    (1,   "I"),
]

class NumeroRomano(NumeroUniversal):
    def __init__(self, literal):
        super().__init__(literal)
        self.tipo = "rom"
        self.permite_fraccion = False
        self.analizar()

    def analizar(self):
        """
        Convierte literal romano a entero (1..100):
        - Valida caracteres (I,V,X,L,C)
        - Aplica regla sustractiva básica (IV=4, IX=9, XL=40, XC=90)
        - Verifica rango final
        """
        texto = self.literal.strip().upper()
        if len(texto) == 0:
            self.valido = False; self.mensaje_error = "Romano vacío"; return

        for ch in texto:
            if ch not in VALOR_ROMANO:
                self.valido = False; self.mensaje_error = "Carácter romano inválido"; return

        total = 0
        i = 0
        while i < len(texto):
            v = VALOR_ROMANO[texto[i]]
            if i + 1 < len(texto):
                v2 = VALOR_ROMANO[texto[i+1]]
                if v < v2:
                    total += (v2 - v)
                    i += 2
                    continue
            total += v
            i += 1

        if total < 1 or total > 100:
            self.valido = False; self.mensaje_error = "Romano fuera de rango (I..C)"; return

        self.valor_decimal = float(total)

    def a_cadena_base_propia(self, valor_decimal):
        """
        Convierte entero 1..100 a romano, usando el mapa ordenado.
        Si no es entero/rango, devuelve etiqueta avisando.
        """
        if not es_entero(valor_decimal):
            return "(no entero)"
        v = a_entero(valor_decimal)
        if v < 1 or v > 100:
            return "(fuera de rango)"
        res = ""
        for val, rom in MAPA_ENTERO_A_ROMANO:
            while v >= val:
                res += rom
                v -= val
        return res
