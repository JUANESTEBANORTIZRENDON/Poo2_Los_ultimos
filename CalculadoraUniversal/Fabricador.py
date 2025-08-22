"""
Fábrica: crea instancias a partir de "tipo:valor".
"""

from Decimales import NumeroDecimal
from Binario import NumeroBinario
from Octal import NumeroOctal
from Hexadecimal import NumeroHexadecimal
from Romano import NumeroRomano

def crear_numero(texto):
    if ":" not in texto:
        d = NumeroDecimal("0"); d.valido = False
        d.mensaje_error = "Formato inválido. Usa 'tipo:valor'"
        return d

    tipo, literal = texto.split(":", 1)
    tipo = tipo.strip().lower()
    literal = literal.strip()

    if tipo == "dec":  return NumeroDecimal(literal)
    if tipo == "bin":  return NumeroBinario(literal)
    if tipo == "oct":  return NumeroOctal(literal)
    if tipo == "hex":  return NumeroHexadecimal(literal)
    if tipo == "rom":  return NumeroRomano(literal)

    d = NumeroDecimal("0"); d.valido = False
    d.mensaje_error = "Tipo desconocido (usa dec/bin/oct/hex/rom)"
    return d
