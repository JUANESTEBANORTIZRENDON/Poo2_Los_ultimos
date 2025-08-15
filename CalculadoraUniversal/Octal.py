
#NumeroOctal: enteros en base 8 (acepta signo '-').


from NumeroUniversal import NumeroUniversal, es_entero, a_entero

class NumeroOctal(NumeroUniversal):
    def __init__(self, literal):
        super().__init__(literal)
        self.tipo = "oct"
        self.analizar()

    def analizar(self):
        texto = self.literal.strip().lower().replace("_", "")
        negativo = False
        if texto.startswith("-"):
            negativo = True; texto = texto[1:]

        #Validacion si esta en octal  octal 
        if len(texto) == 0 or any(ch not in "01234567" for ch in texto):
            self.valido = False; self.mensaje_error = "Octal inválido"; return

        # oct → decimal entero
        valor = 0
        for ch in texto:
            valor = valor * 8 + int(ch)

        if negativo: valor = -valor
        self.valor_decimal = float(valor)

    def a_cadena_base_propia(self, valor_decimal):
        if not es_entero(valor_decimal): return "(no entero)"
        v = a_entero(valor_decimal)
        if v == 0: return "0"
        negativo = v < 0; v = abs(v)
        s = ""
        while v > 0:
            s = str(v % 8) + s
            v //= 8
        if negativo: s = "-" + s
        return s
