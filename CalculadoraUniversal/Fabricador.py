"""
Módulo: fabrica.py
Crea instancias desde texto "tipo:valor" (incluye romanos: 'rom').
"""

from Decimales import NumeroDecimal
from Binario import NumeroBinario
from Octal import NumeroOctal
from Hexadecimal import NumeroHexadecimal
from Romano import NumeroRomano

def crear_numero(texto):
    """
    Retorna una instancia acorde al prefijo:
      - dec: -> NumeroDecimal
      - bin: -> NumeroBinario
      - oct: -> NumeroOctal
      - hex: -> NumeroHexadecimal
      - rom: -> NumeroRomano (I..C)
    En formato inválido/tipo desconocido, retorna NumeroDecimal inválido con mensaje.
    """
    if ":" not in texto:
        d = NumeroDecimal("0"); d.valido = False
        d.mensaje_error = "Formato inválido. Usa 'tipo:valor'"
        return d

    tipo, literal = texto.split(":", 1)
    tipo = tipo.strip().lower()
    literal = literal.strip()

    if tipo == "dec":
        return NumeroDecimal(literal)
    elif tipo == "bin":
        return NumeroBinario(literal)
    elif tipo == "oct":
        return NumeroOctal(literal)
    elif tipo == "hex":
        return NumeroHexadecimal(literal)
    elif tipo == "rom":
        return NumeroRomano(literal)
    else:
        d = NumeroDecimal("0"); d.valido = False
        d.mensaje_error = "Tipo desconocido (usa dec/bin/oct/hex/rom)"
        return d
