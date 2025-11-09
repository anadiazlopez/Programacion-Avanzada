class Libro:

    def __init__(self, titulo, autor, isbn, estado= "?"):
        # Atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
        self.__estado = estado 

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def isbn(self):
        return self.__isbn
    
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter       # Setter para modificar el estado del libro
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    def __str__(self):
        return (f"Título: {self.__titulo}\n"
                f"Autor: {self.__autor}\n"
                f"ISBN: {self.__isbn}\n"
                f"Estado: {self.__estado}")

def lista_libros():
    libro1 = Libro("La ciudad de las sombras", "Victoria Álvarez", "111")
    libro2 = Libro("El sótano", "Natasha Preston", "222")
    libro3 = Libro("Alguien está mintiendo", "Karen M. McManus", "333")
    libro4 = Libro("Harry Potter y el misterio del príncipe", "J.K. Rowling", "444")
    return [libro1, libro2, libro3, libro4]

def prestado_o_disponible(libro):
    info = input("¿Prestado(0) o disponible(1)?: ")
    if info == "0":
        libro.estado = "Prestado"
    elif info == "1":
        libro.estado = "Disponible"
    else:
        print("ERROR EN LA LECTURA DE ESTADO.\n")
        return
    print(f"Estado del libro '{libro.titulo}': {libro.estado}")
    print()

if __name__ == "__main__":
    libros = lista_libros()
    for libro in libros:
        print(libro)
        print()
        prestado_o_disponible(libro)



















