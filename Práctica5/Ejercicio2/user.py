from library import Libreria 
from utils import generar_id_unico
import random

class User:
    def __init__(self, nombre, id, lib_p=None):
        self._nombre = nombre
        self._id = id
        self._libros_prestados = lib_p if lib_p is not None else []

    @property
    def nombre(self):
        return self._nombre

    @property
    def id(self):
        return self._id
    
    @property
    def lista_libros(self):
        return self._libros_prestados
    
    def agregar_libro(self, libro):
        self._libros_prestados.append(libro)
    
    def __str__(self):
        libros_str = ", ".join([f"{libro.titulo} (ISBN: {libro.isbn})" for libro in self._libros_prestados])
        return f"Usuario: {self._nombre}\nID: {self._id}\nLibros prestados:{libros_str if libros_str else 'Ninguno'}\n"


if __name__ == "__main__":
   

    nombre = input("Nombre usuario: ").strip()

    usuario = User(nombre, generar_id_unico(), lib_p=[])  # Inicializar con lista vacía

    biblioteca = Libreria()
    todos_libros = biblioteca.arraylibros  

    for libro in todos_libros:
        libro.estado = random.choice(["Disponible", "Prestado"])

    while True:
        biblioteca.mostrar_libros()
        
        isbn_buscar = input("\nIngrese el ISBN del libro a añadir al usuario (o 'E' para salir): ").strip()

        if isbn_buscar.upper() == 'E':
            print("\nRESUMEN FINAL DEL USUARIO")
            print(usuario)  
            break
        
        libro_encontrado = None
        for libro in todos_libros:
            if libro.isbn == isbn_buscar:
                libro_encontrado = libro
                break
    
        if libro_encontrado:
            if libro_encontrado.estado == "Prestado":
                print(f"El libro '{libro_encontrado.titulo}' ya está prestado.\n")
            else:
                libro_encontrado.estado = "Prestado"
                usuario.agregar_libro(libro_encontrado)
                print(f"Libro '{libro_encontrado.titulo}' prestado.\n")
        else:
            print(f"No se encontró ningún libro con este ISBN.\n")
          
        print(usuario)

        
        