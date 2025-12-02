from practica6 import Empleado, Cliente, RegistroDiario
from time_management import Time 
import utils

def main():
    registro = RegistroDiario()
    
    opciones_menu = [
        "Introducir empleado",
        "Introducir cliente", 
        "Buscar por nombre (y edad)",
        "Mostrar registro diario",
        "Mostrar empleados",
        "Visualizar persona por índice",
        "Combinar registros diarios",
        "Salir"
    ]
    
    while True:
        utils.mostrar_menu(opciones_menu, "REGISTRO DIARIO")
        
        opcion = utils.leer_entero("\nSeleccione una opción (1-8): ", 1, 8)
        
        if opcion == 1:  
            print("\nINTRODUCIR EMPLEADO")
            nombre = utils.leer_cadena("Nombre: ")
            edad = utils.leer_entero("Edad: ")
            hora_nac = utils.leer_entero("Hora (0-23): ", 0, 23)
            minuto_nac = utils.leer_entero("Minuto (0-59): ", 0, 59)
            segundo_nac = utils.leer_entero("Segundo (0-59): ", 0, 59)
            categoria = utils.leer_cadena("Categoría: ")
            antiguedad = utils.leer_entero("Antigüedad (años): ")

            empleado = Empleado(nombre, edad, categoria, antiguedad)
            empleado.nacio.set_time(hora_nac, minuto_nac, segundo_nac, "24 HOURS")
            
            if registro.agregar_persona(empleado):
                print("Empleado agregado al registro.")
            else:
                print("Error al agregar empleado.")
        
        elif opcion == 2:  
            print("\nINTRODUCIR CLIENTE")
            nombre = utils.leer_cadena("Nombre: ")
            edad = utils.leer_entero("Edad: ")
            hora_nac = utils.leer_entero("Hora (0-23): ", 0, 23)
            minuto_nac = utils.leer_entero("Minuto (0-59): ", 0, 59)
            segundo_nac = utils.leer_entero("Segundo (0-59): ", 0, 59)
            dni = utils.leer_cadena("DNI: ")
            
            cliente = Cliente(nombre, edad, dni)
            cliente.nacio.set_time(hora_nac, minuto_nac, segundo_nac, "24 HOURS")
    
            if registro.agregar_persona(cliente):
                print("Cliente agregado al registro.")
            else:
                print("Error al agregar cliente.")
        
        elif opcion == 3:  
            print("\nBUSCAR POR NOMBRE Y EDAD")
            nombre = utils.leer_cadena("Nombre a buscar: ")
            edad = utils.leer_entero("Edad a buscar: ")
            
            resultados = registro.buscar_por_nombre_edad(nombre, edad)
            
            if resultados:
                for persona in resultados:
                    persona.visualizar()
                    if registro.es_empleado(persona):
                        print("\nTipo: EMPLEADO")
                    else:
                        print("\nTipo: CLIENTE")
            else:
                print("\nNo se encontró ninguna persona con ese nombre y edad.")
        
        elif opcion == 4:  
            print("\nREGISTRO DIARIO COMPLETO")
            if len(registro) == 0:
                print("El registro está vacío.")
            else:
                registro.visualizar_registro()
        
        elif opcion == 5:  
            print("\nEMPLEADOS REGISTRADOS")
            registro.visualizar_empleados()
        
        elif opcion == 6:
            print("\nVISUALIZAR PERSONA POR ÍNDICE")
            if len(registro) == 0:
                print("El registro está vacío.")
            else:
                print(f"Hay {len(registro)} personas en el registro.")
                indice = utils.leer_entero(f"Ingrese índice (0-{len(registro)-1}): ", 0, len(registro)-1)
                try:
                    persona = registro[indice]
                    print(f"\nPersona en índice {indice}:")
                    persona.visualizar()
                except IndexError:
                    print(f"Error: Índice fuera de rango.")
        
        elif opcion == 7:  
            print("\nCOMBINAR REGISTROS DIARIOS")
            otro_registro = RegistroDiario()
            
            for i in range(2):
                print(f"\nAñadiendo persona {i+1} al segundo registro:")
                tipo = input("¿Es empleado o cliente? (e/c): ").lower()
                
                if tipo == 'e':
                    nombre = utils.leer_cadena("Nombre: ")
                    edad = utils.leer_entero("Edad: ")
                    hora_nac = utils.leer_entero("Hora (0-23): ", 0, 23)
                    minuto_nac = utils.leer_entero("Minuto (0-59): ", 0, 59)
                    segundo_nac = utils.leer_entero("Segundo (0-59): ", 0, 59)
                    categoria = utils.leer_cadena("Categoría: ")
                    antiguedad = utils.leer_entero("Antigüedad: ")
                    
                    empleado = Empleado(nombre, edad, categoria, antiguedad)
                    empleado.nacio.set_time(hora_nac, minuto_nac, segundo_nac, "24 HOURS")
                    otro_registro.agregar_persona(empleado)
                    
                elif tipo == 'c':
                    nombre = utils.leer_cadena("Nombre: ")
                    edad = utils.leer_entero("Edad: ")
                    hora_nac = utils.leer_entero("Hora (0-23): ", 0, 23)
                    minuto_nac = utils.leer_entero("Minuto (0-59): ", 0, 59)
                    segundo_nac = utils.leer_entero("Segundo (0-59): ", 0, 59)
                    dni = utils.leer_cadena("DNI: ")
                    
                    cliente = Cliente(nombre, edad, dni)
                    cliente.nacio.set_time(hora_nac, minuto_nac, segundo_nac, "24 HOURS")
                    otro_registro.agregar_persona(cliente)
                
                else:
                    print("Opción no válida. Se cancela la operación.")
                    break
            
            if len(otro_registro) == 2:
                registro_combinado = registro + otro_registro
                print(f"\nRegistro actual: {len(registro)} personas")
                print(f"Nuevo registro: {len(otro_registro)} personas")
                print(f"Total combinado: {len(registro_combinado)} personas")
                registro._personas = registro_combinado._personas
                print("Registros combinados exitosamente.")
            else:
                print("\nNo se pudo completar la combinación.")
        
        elif opcion == 8:
            break

if __name__ == "__main__":
    main()