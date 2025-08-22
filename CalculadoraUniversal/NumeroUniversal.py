"""
Clase Padre 'NumeroUniversal'.
Contiene utilidades como MÉTODOS de instancia: es_entero / a_entero.
Todas las subclases usan self.es_entero(...) y self.a_entero(...).
"""

class NumeroUniversal:
    def __init__(self, literal):
        self.literal = str(literal)
        self.valido = True
        self.mensaje_error = ""
        self.valor_decimal = 0.0
        self.tipo = "base"
        self.permite_fraccion = False

    # ----- Métodos que implementan/usan las subclases -----
    def analizar(self):
        """Las subclases convierten self.literal -> self.valor_decimal y validan."""
        pass

    def a_cadena_base_propia(self, valor_decimal):
        """Las subclases formatean el valor_decimal a su base."""
        return str(valor_decimal)

    def convertir_a(self, clase_destino):
        """
        Convierte este número a 'clase_destino'.
        Si el destino no permite fracciones y el valor no es entero -> regresa Decimal.
        """
        numero_dest = clase_destino("0")

        if not numero_dest.permite_fraccion:
            if not self.es_entero(self.valor_decimal):
                # IMPORTA DESDE TU MÓDULO DE DECIMALES
                from Decimales import NumeroDecimal
                d = NumeroDecimal("0")
                d.valor_decimal = self.valor_decimal
                return d

        texto_en_destino = numero_dest.a_cadena_base_propia(self.valor_decimal)
        convertido = clase_destino(texto_en_destino)
        convertido.valor_decimal = self.valor_decimal
        return convertido

    def __str__(self):
        if not self.valido:
            return "ERROR: " + self.mensaje_error
        return self.a_cadena_base_propia(self.valor_decimal) + " (" + self.tipo + ")"

    # ----- Utilidades para las subclases -----
    def es_entero(self, valor_decimal):
        """True si valor_decimal es (o está muy cerca de) un entero."""
        if isinstance(valor_decimal, int):
            return True
        if abs(valor_decimal - round(valor_decimal)) < 1e-9:
            return True
        return False

    def a_entero(self, valor_decimal):
        """Redondea un float 'casi entero' a int."""
        return int(round(valor_decimal))
