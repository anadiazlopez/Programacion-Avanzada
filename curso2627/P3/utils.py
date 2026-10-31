import matriz

def leer_int(mensaje = "Introduce un número entero: "):
    """
    Función auxiliar que lee un número entero del teclado.
    Si se introduce un valor no válido, se solicita de nuevo.

    Parámetros:
        mensaje # El mensaje que se muestra al usuario
        # solicitando la entrada (str). Por defecto
        # "Introduce un número entero: "
    Devuelve:
    int: El valor entero introducido por el usuario.
    """
    entrada = input(mensaje)
    while not entrada.isdigit():
        print("\n¡Error! Introduce un número entero.")
        entrada = input(mensaje)
    return int(entrada)

def leer_float(mensaje = "Introduce un número decimal: "):
    """
    Función auxiliar que solicita al usuario un número decimal.
    Si se introduce un valor no válido, se solicitar de nuevo.
    Parámetros:
    mensaje # El mensaje que se muestra al usuario
    # solicitando la entrada (str). Por defecto
    # "Introduce un número decimal: "
    Devuelve:
    El valor decimal introducido por el usuario (float)
    """
    entrada = input(mensaje)
    while not entrada.isdigit():
        print("\n¡Error! Introduce un número decimal.")
        entrada = input(mensaje)
    return float(entrada)

def crear_menu(opciones_menu):
    """
    Función que muestra un menú de opciones y solicita al usuario
    que seleccione una opción válida.
    Parámetros:
    opciones_menu # lista de opciones a mostrar en el menú
    # (list)
    Devuelve:
    El número de opción seleccionado por el usuario (int)
    """
    for i, opcion in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion}.")
    
    while True:
        opcion = leer_int("\nSelecciona una opción: ")
        if 1 <= opcion <= len(opciones_menu):
            return opcion
        print("\n¡¡Opción incorrecta!!")

def main():
    opciones_principales = [
        "Construir matriz 1D",
        "Construir matriz 2D",
        "Construir matriz identidad",
        "Introducir matriz",
        "Mostrar matriz",
        "Operaciones con matrices",
        "Finalizar el programa"
    ]

    opciones_submenu = [
        "Sumar matrices",
        "Restar matrices",
        "Volver al menú principal"
    ]

    mi_matriz = matriz.MatrizFloat()
    
    while True:
        print('\n\tMENÚ')
        opcion = crear_menu(opciones_principales)

        if opcion == 1:
            n = leer_int("\nIntroduce el número de elementos: ")
            mi_matriz.crear_matriz1D(n)

        elif opcion == 2:
            nfil = leer_int("\nIntroduce el número de filas: ")
            ncol = leer_int("Introduce el número de columnas: ")
            mi_matriz.crear_matriz2D(nfil, ncol)

        elif opcion == 3:
            n = leer_int("\nIntroduce el tamaño de la matriz identidad: ")
            mi_matriz = matriz.MatrizFloat.matriz_identidad(n)

        elif opcion == 4:
            mi_matriz.introducir()

        elif opcion == 5:
            mi_matriz.mostrar()

        elif opcion == 6:
            while True:
                print('\n\tSUBMENÚ')
                opcion_sub = crear_menu(opciones_submenu)
                
                if opcion_sub == 1:
                    if not mi_matriz.existe():
                        print("\n¡Error! La matriz principal no existe o está vacía.")
                    else:
                        nfil = leer_int("\nIntroduce el número de filas de la segunda matriz: ")
                        ncol = leer_int("Introduce el número de columnas de la segunda matriz: ")
                        
                        otra_matriz = matriz.MatrizFloat()
                        otra_matriz.crear_matriz2D(nfil, ncol)
                        print("\nIntroduce los valores para la segunda matriz:")
                        otra_matriz.introducir()
                        
                        resultado = mi_matriz.sumar_matrices(otra_matriz)
                        if resultado is not None:
                            print("\nResultado de la suma:")
                            resultado.mostrar()
                            mi_matriz = resultado # Actualizar matriz principal

                elif opcion_sub == 2:
                    if not mi_matriz.existe():
                        print("\n¡Error! La matriz principal no existe o está vacía.")
                    else:
                        nfil = leer_int("\nIntroduce el número de filas de la segunda matriz: ")
                        ncol = leer_int("Introduce el número de columnas de la segunda matriz: ")
                        
                        otra_matriz = matriz.MatrizFloat()
                        otra_matriz.crear_matriz2D(nfil, ncol)
                        print("\nIntroduce los valores para la segunda matriz:")
                        otra_matriz.introducir()
                        
                        resultado = mi_matriz.restar_matrices(otra_matriz)
                        if resultado is not None:
                            print("\nResultado de la resta:")
                            resultado.mostrar()
                            mi_matriz = resultado   # Actualizar matriz principal

                elif opcion_sub == 3:
                    break 

        elif opcion == 7:
            print("\nFinalizando el programa...")
            break

if __name__ == "__main__":
    main()