"""
NumeroDecimal: acepta enteros, decimales y fracciones 'a/b'.

"""

from NumeroUniversal import NumeroUniversal

class NumeroDecimal(NumeroUniversal):
    def __init__(self, literal):
        super().__init__(literal)
        self.tipo = "dec"
        self.permite_fraccion = True
        self.analizar()

    def analizar(self):
        texto = self.literal.strip().lower()
        if "/" in texto:
            partes = texto.split("/")
            if len(partes) == 2 and partes[0].replace("-", "").isdigit() and partes[1].isdigit() and partes[1] != "0":
                num = int(partes[0]); den = int(partes[1])
                self.valor_decimal = float(num) / float(den)
            else:
                self.valido = False
                self.mensaje_error = "Fracción decimal inválida"
                return
        else:
            puntos = texto.count(".")
            if puntos > 1 or len(texto) == 0:
                self.valido = False
                self.mensaje_error = "Decimal inválido"
                return
            for i, ch in enumerate(texto):
                if ch.isdigit() or ch == "." or (ch == "-" and i == 0):
                    continue
                self.valido = False
            if self.valido:
                self.valor_decimal = float(texto)

    def a_cadena_base_propia(self, valor_decimal):
        if self.es_entero(valor_decimal):
            return str(self.a_entero(valor_decimal))
        return ("{:.10f}".format(valor_decimal)).rstrip("0").rstrip(".")
