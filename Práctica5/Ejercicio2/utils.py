import uuid
from typing import List, Optional

def leer_int(mensaje="Introduce un número entero: "):
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

def leer_float(mensaje="Introduce un número decimal: "):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Por favor, introduce un número decimal válido.")

def crear_menu(opciones_menu):
    print("MENÚ PRINCIPAL\n")
    
    for i, opcion in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion}")
    
    print("\n")
    
    while True:
        try:
            seleccion = int(input("Selecciona una opción: "))
            if 1 <= seleccion <= len(opciones_menu):
                return seleccion
            else:
                print(f"Error: Por favor, selecciona una opción entre 1 y {len(opciones_menu)}")
        except ValueError:
            print("Error: Por favor, introduce un número válido.")

def generar_id_unico():
    id_completo = str(uuid.uuid4())
    return id_completo[:8]