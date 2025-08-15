"""
Clase Padree 'NumeroUniversal' .
"""
#Validacion si es entero y el decimal 
def es_entero(valor_decimal):
    """Devuelve True si valor_decimal es (o está muy cerca de) un entero."""
    if isinstance(valor_decimal, int):
        return True
    #Validamos decimal restandole el entero redondeado del numero y si se puede aproximar se aproxima al entero mas cercanaoo
    if abs(valor_decimal - int(round(valor_decimal))) < 1e-9:
        return True
    return False

#se convierte decimal float a entero 
def a_entero(valor_decimal):
    """Redondea un float casi entero a int."""
    return int(round(valor_decimal))


class NumeroUniversal:
    """
    Clase base para números de distintas bases.
    Guarda: literal (texto original), flags de validez, valor_decimal (float),
    etiqueta de tipo y si permite fracciones (solo decimal=True).
    """
    def __init__(self, literal):
        self.literal = str(literal)
        self.valido = True
        self.mensaje_error = ""
        self.valor_decimal = 0.0
        self.tipo = "base"
        self.permite_fraccion = False

#Funsiones que se heredaran 
    def analizar(self):
        """Subclases implementan: convertir literal a valor_decimal y validar."""
        pass

    def a_cadena_base_propia(self, valor_decimal):
        """
        Convierte un valor decimal canónico (float/int) a texto en su base.
        Las subclases lo sobreescriben.
        """
        return str(valor_decimal)

    def convertir_a(self, clase_destino):
        """
        Convierte a otra clase de número.
        Si el destino no permite fracciones y el valor no es entero -> devuelve Decimal.
        """
        numero = clase_destino("0")
        if not numero.permite_fraccion:
            if not es_entero(self.valor_decimal):
                from NumeroUniversal import NumeroDecimal
                d = NumeroDecimal("0")
                d.valor_decimal = self.valor_decimal
                return d

        texto = numero.a_cadena_base_propia(self.valor_decimal)
        numero = clase_destino(texto)
        numero.valor_decimal = self.valor_decimal
        return numero

#metodo en caso de que el valor no sea valido 
    def __str__(self):
        if not self.valido:
            return "ERROR: " + self.mensaje_error
        return self.a_cadena_base_propia(self.valor_decimal) + " (" + self.tipo + ")"
