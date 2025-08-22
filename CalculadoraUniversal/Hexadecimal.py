"""
NumeroHexadecimal: enteros en base 16 (acepta '-').
"""

from NumeroUniversal import NumeroUniversal

class NumeroHexadecimal(NumeroUniversal):
    def __init__(self, literal):
        super().__init__(literal)
        self.tipo = "hex"
        self.analizar()

    def analizar(self):
        texto = self.literal.strip().lower().replace("_", "")
        negativo = False
        if texto.startswith("-"):
            negativo = True; texto = texto[1:]
        if len(texto) == 0 or any(ch not in "0123456789abcdef" for ch in texto):
            self.valido = False; self.mensaje_error = "Hexadecimal inválido"; return
        mapa = {"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
        valor = 0
        for ch in texto:
            valor = valor * 16 + (int(ch) if ch.isdigit() else mapa[ch])
        if negativo: valor = -valor
        self.valor_decimal = float(valor)

    def a_cadena_base_propia(self, valor_decimal):
        if not self.es_entero(valor_decimal):
            return "(no entero)"
        v = self.a_entero(valor_decimal)
        if v == 0: return "0"
        negativo = v < 0; v = abs(v)
        digitos = "0123456789abcdef"
        s = ""
        while v > 0:
            s = digitos[v % 16] + s
            v //= 16
        if negativo: s = "-" + s
        return s
