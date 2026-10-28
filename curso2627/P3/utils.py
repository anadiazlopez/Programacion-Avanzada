
def menu():
    print("MENÚ")
    print("1. Construir matriz 1D.")
    print("2. Construir matriz 2D.")
    print("3. Construir matriz identidad.")
    print("4. Introducir matriz.")
    print ("5. Mostrar matriz")
    print("6. Operaciones con matrices")
    print("7. Terminar: finaliza el programa.")

    opcion = input("Selecciona una opción (1 - 7):")
    return opcion

def main():

    opcion = menu()

    if opcion == 1:
        pass
    if opcion == 2:
        pass
    if opcion == 3:
        pass
    if opcion == 4:
        pass
    if opcion == 5:
        pass
    if opcion == 6:
        print("SUBMENÚ")
        print("1. Sumar matrices.")
        print("2. Restar matrices")
        print("3. Volver al menú principal.")
        opcion_sub = input("Selecciona una opción (1 - 3):")
        if opcion_sub == 1:
            pass
        if opcion_sub == 2:
            pass
        if opcion_sub == 3:
            main()
    if opcion == 7:
        pass

if __name__ == "__main__":
    main()