
#NumeroBinario: enteros en base 2 (acepta signo '-').


from NumeroUniversal import NumeroUniversal, es_entero, a_entero

class NumeroBinario(NumeroUniversal):
    def __init__(self, literal):
        super().__init__(literal)
        self.tipo = "bin"
        self.analizar()

    def analizar(self):
        #replace hace la misma funsion que strip solo que especifica el guion medio para guiones dentro de la lista 
        texto = self.literal.strip().lower().replace("_", "")
        negativo = False
        if texto.startswith("-"):
            negativo = True; texto = texto[1:]

        if len(texto) == 0 or any(ch not in "01" for ch in texto):
            self.valido = False; self.mensaje_error = "Binario inválido"; return

        # bin → decimal entero
        valor = 0
        for ch in texto:
            valor = valor * 2 + (1 if ch == "1" else 0)

        if negativo: valor = -valor
        self.valor_decimal = float(valor)

    def a_cadena_base_propia(self, valor_decimal):
        if not es_entero(valor_decimal): return "(no entero)"
        v = a_entero(valor_decimal)
        if v == 0: return "0"
        negativo = v < 0; v = abs(v)
        bits = ""
        while v > 0:
            '''Agrega "1" al inicio de la cadena 'bits' si el resto de dividir v entre 2 es 1 (bit impar), 
             de lo contrario agrega "0"; luego actualiza v con la división entera entre 2 para seguir el proceso.'''
            bits = ("1" if (v % 2 == 1) else "0") + bits
            v //= 2
        if negativo: bits = "-" + bits
        return bits
