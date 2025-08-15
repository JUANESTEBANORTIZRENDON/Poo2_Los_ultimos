# =================
# Archivo: main.py
# =================
"""
Punto de entrada con menú (estilo switch con if/elif).
- Soporta tipos: dec, bin, oct, hex, rom (romano I..C).
- Bucle para realizar varias operaciones hasta que el usuario decida salir.
"""

from Calculadora import Calculadora
from Fabricador import crear_numero

def seleccionar_tipo(tipo):
    """Valida el tipo ingresado; retorna el tipo o '' si es inválido."""
    if tipo in ("dec", "bin", "oct", "hex", "rom"):
        return tipo
    return ""

def seleccionar_operacion(op):
    """Valida operación; retorna el símbolo o '' si es inválida."""
    if op in ("+", "-", "*", "/"):
        return op
    return ""

def ejecutar():
    print("=== Calculadora Numérica Universal ===")
    print('Para selecionar escribe el contenido interno de los parentesi exactamente igual de cada opcion correspondiente ')
    print("Tipos: Decimal (dec),\n Binario (bin),\n Octal (oct),\n Hexadecimal (hex),\n Romano (rom )")
    print('--------------------------------------------------------------------------------------------------')
    print("Operaciones: +, -, *, /   (si el operando izquierdo es rom, solo +)")
    print('--------------------------------------------------------------------------------------------')

    while True:
        # Selección de tipo (mismo para ambos operandos, como pediste)
        tipo_elegido = input("\nTipo de número para ambos operandos: ").strip().lower()
        tipo_elegido = seleccionar_tipo(tipo_elegido)
        if tipo_elegido == "":
            print("ERROR: tipo inválido (usa dec/bin/oct/hex/rom)")
            continue

        # Entrada de valores y operación
        valor1 = input("Primer valor: ").strip()
        valor2 = input("Segundo valor: ").strip()
        operacion = input("Operación (+, -, *, /): ").strip()
        operacion = seleccionar_operacion(operacion)
        if operacion == "":
            print("ERROR: operación inválida (usa +, -, *, /)")
            continue

        # Crear números
        num1 = crear_numero(f"{tipo_elegido}:{valor1}")
        num2 = crear_numero(f"{tipo_elegido}:{valor2}")

        # Calcular
        calc = Calculadora()
        resultado = calc.operar(num1, num2, operacion)

        # Mostrar resultados
        print("\n=== Resultados ===")
        print("Operando 1:", num1)
        print("Operando 2:", num2)
        print("Resultado:", resultado)

        # Conversión opcional de resultado
        convertir = input("\n¿Convertir resultado a otra base? (dec/bin/oct/hex/rom o Enter para omitir): ").strip().lower()
        convertir = seleccionar_tipo(convertir)
        if convertir != "":
            # Imports locales para evitar dependencias si no se convierte
            from Decimales import NumeroDecimal
            from Binario import NumeroBinario
            from Octal import NumeroOctal
            from Hexadecimal import NumeroHexadecimal
            from Romano import NumeroRomano

            if convertir == "dec":
                print("Convertido:", resultado.convertir_a(NumeroDecimal))
            elif convertir == "bin":
                print("Convertido:", resultado.convertir_a(NumeroBinario))
            elif convertir == "oct":
                print("Convertido:", resultado.convertir_a(NumeroOctal))
            elif convertir == "hex":
                print("Convertido:", resultado.convertir_a(NumeroHexadecimal))
            elif convertir == "rom":
                print("Convertido:", resultado.convertir_a(NumeroRomano))
        else:
            print("Conversión omitida.")

        # ¿otra operación?
        seguir = input("\n¿Desea realizar otra operación? (s/n): ").strip().lower()
        if seguir != "s":
            print("Cerrando calculadora...")
            break

if __name__ == "__main__":
    ejecutar()

