from book import Libro, lista_libros, prestado_o_disponible
import random

class Libreria:
    def __init__(self):
        self.arraylibros = []
        libros_base = lista_libros()

        for libro in libros_base:
            libro.estado = random.choice(["Disponible", "Prestado"])

        self.arraylibros = libros_base

    def lista(self, libro): 
        print(f"Título: {libro.titulo}")
        print(f"Autor: {libro.autor}")
        print(f"ISBN: {libro.isbn}")
        print(f"Estado: {libro.estado}")
        print("\n")
        

    def mostrar_libros(self):
        print("LISTA DE LIBROS")
    
        for i, libro in enumerate(self.arraylibros, 1):
            self.lista(libro)
        return False    
    
    def agregar_libro(self):
        titulo = input("Ingrese el título del libro: ").strip()
        autor = input("Ingrese el autor del libro: ").strip()
        isbn = input("Ingrese el ISBN del libro: ").strip()

        nuevo_libro = Libro(titulo, autor, isbn, "?")

        for libro_existente in self.arraylibros:
            if libro_existente.isbn == nuevo_libro.isbn:
                print("Ya existe este libro.\n")
                return False
        
        prestado_o_disponible(nuevo_libro)

        self.arraylibros.append(nuevo_libro)
        self.mostrar_libros()
        print(f"Libro '{nuevo_libro.titulo}' agregado :D\n")
        return True
  
    def eliminar_libro(self):
        isbn = input("Introduzca el ISBN del libro que desea eliminar: ").strip()
        for i, libro_existente in enumerate(self.arraylibros):                  # Obtiene índice + libro
            if libro_existente.isbn == isbn:
                libro_eliminado = self.arraylibros.pop(i)
                self.mostrar_libros()                                     # Elimina la posición exacta del libro
                print(f"Libro '{libro_eliminado.titulo}' ha sido eliminado correctamente.\n")
                return True

        print(f"No se encontró ningún libro con ISBN: {isbn}")
        return False

    def prestar_libro(self):
        isbn = input("Introduzca el ISBN del libro que desea prestar: ").strip()
        
        for libro in self.arraylibros:
            if libro.isbn == isbn:
                if libro.estado == "Prestado":
                    print(f"El libro '{libro.titulo}' ya está prestado.\n")
                    return False
                else:
                    libro.estado = "Prestado"
                    self.mostrar_libros()
                    print(f"Libro '{libro.titulo}' prestado correctamente.\n")
                    return True
        
        print(f"No se encontró ningún libro con ISBN: {isbn}")
        return False

    def devolver_libro(self):
        isbn = input("Introduzca el ISBN del libro que desea devolver: ").strip()
        
        for libro in self.arraylibros:
            if libro.isbn == isbn:
                if libro.estado == "Disponible":
                    print(f"El libro '{libro.titulo}' ya está disponible.\n")
                    return False
                else:
                    libro.estado = "Disponible"
                    self.biblioteca.mostrar_libros()
                    print(f"\nLibro '{libro.titulo}' devuelto correctamente.\n")
                    return True
        
        print(f"No se encontró ningún libro con ISBN: {isbn}")
        return False
    
    def buscar_libro(self):
        buscar = input("¿Desea bucar un libro por título(0) o por autor(1)?: ")
        if buscar == "0":
            titulo = input("Introduce título a buscar: ")
            print("\n")
            for libro in self.arraylibros:
                if titulo.lower() == libro.titulo.lower():
                    self.lista(libro)
        elif buscar == "1":
            autor = input("Introduce autor a buscar: ")
            print("\n")
            for libro in self.arraylibros:
                if autor.lower() == libro.autor.lower():
                    self.lista(libro)
        else:
            print("\nNo se encontró ningún libro.\n")
        return False































































