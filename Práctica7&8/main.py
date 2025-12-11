from publicaciones import Libro, Revista  
from excepciones import ErrorBiblioteca
from Utils import validar_titulo, validar_anio, guardar_publicaciones, cargar_publicaciones

# C:\Users\anadi\Desktop\uni\2025-2026\PRIMER CUATRIMESTRE\PROGRAMACIÓN AVANZADA\PRÁCTICA 7-8- PROGRA/biblioteca.dat

import os  

publicaciones = []


def anadir():
    tipo = input("¿Libro (L) o Revista (R)?").upper()
    try:
        titulo = input("Título: ")
        validar_titulo(titulo)
        autor = input("Autor: ")
        if not autor.strip():
            raise ValueError("El autor no puede estar vacío")
        anio = input("Año: ")
        validar_anio(anio)
        anio = int(anio)

        if tipo == "L":
            genero = input("Género: ")
            if not genero.strip():
                raise ValueError("El género no puede estar vacío")
            publicaciones.append(Libro(titulo, autor, anio, genero))
        elif tipo == "R":
            num_edicion = input("Número de edición: ")
            if not num_edicion.isdigit():
                raise ValueError("El número de edición debe ser un entero")
            publicaciones.append(Revista(titulo, autor, anio, int(num_edicion)))
        else:
            print("Tipo no válido")
    except ValueError as e:
        print(f"Error: {e}")

def mostrar():
    if not publicaciones:
            print("No hay publicaciones registradas.")
    else:
        for i, pub in enumerate(publicaciones, 1):
            print(f"\n----------------------------------------------\n{i}. {pub.descripcion()}")

def guardar():
    if not publicaciones:
        print("No hay publicaciones para guardar.")
        return
    nombre_archivo = input("Nombre del archivo para guardar: ")
    try:
        guardar_publicaciones(publicaciones, nombre_archivo)
    except ErrorBiblioteca as e:
        print(f"Error: {e}")

def cargar():
    global publicaciones
    nombre_archivo = input("Nombre del archivo a cargar: ")
    try:
        publicaciones = cargar_publicaciones(nombre_archivo)
    except ErrorBiblioteca as e:
        print(f"Error: {e}")

def main():
    while True:
        print("\n--- MENÚ BIBLIOTECA DIGITAL ---")
        print("1. Añadir publicaciones (libros o revistas)")
        print("2. Mostrar publicaciones disponibles.")
        print("3. Guardar publicaciones en un fichero.")
        print("4. Cargar publicaciones desde un fichero.")
        print("5. Salir.")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            anadir()
        if opcion == "2":
            mostrar()
        if opcion == "3":
            guardar() 
        if opcion == "4":
            cargar()
        if opcion == "5":
            break

if __name__ == "__main__":
    main()




























