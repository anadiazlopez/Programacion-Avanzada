from library import Libreria

def mostrar_menu():
    print("BIBLIOTECA\n")
    print("1. Agregar libro.")
    print("2. Eliminar libro.")
    print("3. Prestar libro.")
    print("4. Devolver libro.")
    print("5. Buscar libro.")
    print("6. Mostrar lista de libros.")
    print("7. SALIR.\n")
    return input("Seleccione una opción: ") 

if __name__ == "__main__":
    biblioteca = Libreria()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            biblioteca.agregar_libro()

        elif opcion == "2":
            biblioteca.eliminar_libro()
        
        elif opcion == "3":
            biblioteca.prestar_libro()

        elif opcion == "4":
            biblioteca.devolver_libro()
            
        elif opcion == "5":
            biblioteca.buscar_libro()  

        elif opcion == "6":
            biblioteca.mostrar_libros()

        elif opcion == "7":
            break  

        else:
            print("Opción inválida.")