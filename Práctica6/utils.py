def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"Error: El valor debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and valor > maximo:
                print(f"Error: El valor debe ser menor o igual a {maximo}")
                continue
            return valor
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")

def leer_cadena(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Error: La cadena no puede estar vacía.")

def mostrar_menu(opciones, titulo="MENÚ"):
    print(f"\n\n")
    print(titulo)
    for i, opcion in enumerate(opciones, 1):
        print(f"{i}. {opcion}")
