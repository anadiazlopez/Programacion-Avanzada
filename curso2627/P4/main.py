# import utils -------- poner utils.funcion()
from utils import leer_int, leer_float, crear_menu, leer_cadena
from ficha import Ficha
from cliente import Cliente
from registroDiario import RegistroDiario
from time_management import Time
from empleado import Empleado
from datetime import date

def datos_ficha():
    nombre = leer_cadena('\nIntroduce nombre: ')
    edad = leer_int('Introduce su edad: ')
    while True:
        cadena_hora = input("Introduce hora de nacimiento (HH:MM:SS FORMATO): ")
        nacio = Time.from_string(cadena_hora)

        if nacio is not None:
            break 
        
        print("\nLa cadena debe ser HH:MM:SS y formato correcto.\n")
    return nombre, edad, nacio

def main():
    opciones = [
        "Introducir empleado",
        "Introducir cliente",
        "Buscar por nombre (y edad)",
        "Mostrar registro diario",
        "Mostrar empleados",
        "Visualizar persona por índice",
        "Combinar registros diarios",
        "Salir"
    ]
       
    registroDiario = RegistroDiario()  
    
    while True:
        print('\n\tMENÚ')
        opcion = crear_menu(opciones)

        if opcion == 1:
            nombre, edad, nacio = datos_ficha()
            while True:
                try:
                    categoria = leer_cadena("Introduce la categoría: ")
                    empleado = Empleado(nombre, edad, nacio, categoria, 0)
                    break 
                except ValueError as e:
                    print(e)

            antiguedad = leer_int('¿Cuántos años lleva el empleado? (0 si lleva meses): ')
            empleado.antiguedad = antiguedad 
            registroDiario.agregar_persona(empleado)
        
        elif opcion == 2:
            nombre, edad, nacio = datos_ficha()
            while True:
                try:
                    dni = leer_cadena("Introduce el DNI: ")
                    cliente = Cliente(nombre, edad, nacio, dni)
                    break  
                except ValueError as e:
                    print(e)  
            registroDiario.agregar_persona(cliente)

        elif opcion == 3:
            nombre = leer_cadena("Introduce el nombre a buscar: ")
            edad= leer_int("Introduce la edad a buscar: ")

            for persona in registroDiario.personas:
                if persona.nombre.lower() == nombre.lower() and persona.edad == edad:
                    if registroDiario.es_empleado(persona):
                        print("\t\nEMPLEADO")
                    else:
                        print("\t\nCLIENTE")
                    persona.visualizar()
                    print("\n", "=*" * 30)
                    break
            else: 
                print("\nNo se ha encontrado a ninguna persona con ese nombre y edad.\n")

        elif opcion == 4:
            if not registroDiario.personas:
                print("\nEl registro está vacío.\n")
            else:
                print(f"\nREGISTRO DE HOY {date.today()}:")
                registroDiario.visualizar_registro()

        elif opcion == 5:
            if not registroDiario.personas:
                print("\nEl registro de empleados está vacío.\n")
            else:
                registroDiario.visualizar_empleados()

        elif opcion == 6:
            if len(registroDiario.personas) == 0:
                print("\nEl registro está vacío.\n")
            else:
                indice = leer_int("Introduce el índice: ")
                if 0 <= indice < len(registroDiario.personas):
                    persona = registroDiario[indice]
                    persona.visualizar()
                    print("\n", "=*" * 30)
                else:
                    print("\nÍndice incorrecto.\n")
        
        elif opcion == 7:
            otro_registro = RegistroDiario()
            registro_total = registroDiario + otro_registro
            registro_total.visualizar_registro()

        elif opcion == 8:
            print("\nSaliendo del programa...")
            break

if __name__ == "__main__":
    main()