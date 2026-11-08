
def leer_cadena(mensaje):
    entrada = input(mensaje)
    while not entrada.strip():  # Quita espacios en blanco
        print("\nIntroduce una cadena.\n")
        entrada = input(mensaje)
    return entrada

def leer_int(mensaje = "Introduce un número entero: "):
    entrada = input(mensaje)
    while not entrada.isdigit():
        print("\nIntroduce un número entero.\n")
        entrada = input(mensaje)
    return int(entrada)

def leer_float(mensaje = "Introduce un número decimal: "):
    entrada = input(mensaje)
    while not entrada.isdigit():
        print("\nIntroduce un número decimal.\n")
        entrada = input(mensaje)
    return float(entrada)

def crear_menu(opciones_menu):
    for i, opcion in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion}.")
    while True:
        opcion = leer_int("\nSelecciona una opción: ")
        if 1 <= opcion <= len(opciones_menu):
            return opcion
        print("\n¡¡Opción incorrecta!!\n")

