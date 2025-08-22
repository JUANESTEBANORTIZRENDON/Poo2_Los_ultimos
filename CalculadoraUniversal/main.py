"""
Menú con dos modos: Calculadora (cal) y Convertidor (con).
Tipos: dec, bin, oct, hex, rom (I..C).
"""

from Calculadora import Calculadora
from Fabricador import crear_numero

def seleccionar_tipo(t):
    return t if t in ("dec", "bin", "oct", "hex", "rom") else ""

def seleccionar_operacion(op):
    return op if op in ("+", "-", "*", "/") else ""

def ejecutar():
    print("=== Calculadora / Convertidor Numérico Universal ===")
    print("Modos: cal (calculadora) | con (convertidor)")

    while True:
        modo = input("\nEscribe el modo (cal / con): ").strip().lower()

        if modo == "cal":
            tipo = seleccionar_tipo(input("Tipo para ambos operandos (dec/bin/oct/hex/rom): ").strip().lower())
            if tipo == "": print("ERROR: tipo inválido"); continue

            v1 = input("Primer valor: ").strip()
            v2 = input("Segundo valor: ").strip()
            op = seleccionar_operacion(input("Operación (+, -, *, /): ").strip())
            if op == "": print("ERROR: operación inválida"); continue

            n1 = crear_numero(f"{tipo}:{v1}")
            n2 = crear_numero(f"{tipo}:{v2}")

            calc = Calculadora()
            res = calc.operar(n1, n2, op)

            print("\n=== Resultados ===")
            print("Operando 1:", n1)
            print("Operando 2:", n2)
            print("Resultado :", res)

            dst = seleccionar_tipo(input("\n¿Convertir resultado? (dec/bin/oct/hex/rom o Enter): ").strip().lower())
            if dst != "":
                from Decimales import NumeroDecimal
                from Binario import NumeroBinario
                from Octal import NumeroOctal
                from Hexadecimal import NumeroHexadecimal
                from Romano import NumeroRomano

                if dst == "dec": print("Convertido:", res.convertir_a(NumeroDecimal))
                elif dst == "bin": print("Convertido:", res.convertir_a(NumeroBinario))
                elif dst == "oct": print("Convertido:", res.convertir_a(NumeroOctal))
                elif dst == "hex": print("Convertido:", res.convertir_a(NumeroHexadecimal))
                elif dst == "rom": print("Convertido:", res.convertir_a(NumeroRomano))
            else:
                print("Conversión omitida.")

        elif modo == "con":
            print("\n=== MODO CONVERTIDOR ===")
            tipo_src = seleccionar_tipo(input("Tipo del número a convertir (dec/bin/oct/hex/rom): ").strip().lower())
            if tipo_src == "": print("ERROR: tipo inválido"); continue

            val_src = input("Valor a convertir: ").strip()
            num = crear_numero(f"{tipo_src}:{val_src}")
            if not num.valido:
                print("ERROR:", num.mensaje_error); continue

            tipo_dst = seleccionar_tipo(input("¿Convertir a qué base? (dec/bin/oct/hex/rom): ").strip().lower())
            if tipo_dst == "": print("ERROR: tipo destino inválido"); continue

            from Decimales import NumeroDecimal
            from Binario import NumeroBinario
            from Octal import NumeroOctal
            from Hexadecimal import NumeroHexadecimal
            from Romano import NumeroRomano

            if tipo_dst == "dec": print("Convertido:", num.convertir_a(NumeroDecimal))
            elif tipo_dst == "bin": print("Convertido:", num.convertir_a(NumeroBinario))
            elif tipo_dst == "oct": print("Convertido:", num.convertir_a(NumeroOctal))
            elif tipo_dst == "hex": print("Convertido:", num.convertir_a(NumeroHexadecimal))
            elif tipo_dst == "rom": print("Convertido:", num.convertir_a(NumeroRomano))

        else:
            print("Opción inválida. Escribe 'cal' o 'con'.")
            continue

        seguir = input("\n¿Desea realizar otra acción? (s/n): ").strip().lower()
        if seguir != "s":
            print("Cerrando programa...")
            break

if __name__ == "__main__":
    ejecutar()
