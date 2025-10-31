import numpy as np
class CMatFloat:
    """
    Clase que representa una matriz dinámica 1D/2D.
    Atributos:
    _Matriz # Almacena la matriz (utilice numpy)
    _m_nFilas # Almacena el número de filas de la matriz
    _m_nColumnas # Almacena el número de columnas de la matriz
    """
    def __init__(self):
        """
        Método para inicializar el atributo matriz con None
        Y los atributos filas y columnas a 0.
        """
        self.matriz = None
        self.num_filas = 0
        self.num_columnas = 0

    def CrearMatriz2D(self, nFilas, nColumnas):
        """
        Método para crear una matriz bidimensional de ceros.
        Asigna valores de filas y columnas según parámetros.
        """
        self.matriz =np.zeros((nFilas,nColumnas)) # np.zeros() es una función de numpy que crea una matriz (array) llena de ceros.
        self.num_filas = nFilas
        self.num_columnas = nColumnas

    def CrearMatriz1D(self, nElementos):
        """
        Método para crear una matriz unidimensional de ceros.
        Usa CrearMatriz2D para asignar 1 fila y n columnas.
        """
        self.CrearMatriz2D(1, nElementos)

    def Introducir(self):
        """
        Método para introducir los elementos de la matriz.
        Los elementos de la matriz son de tipo decimal.
        """
        if not self.Existe():
            print("La matriz no existe. Cree una matriz primero.")
            return
        
        print(f"Introduzca los elementos de la matriz ({self.num_filas}x{self.num_columnas}):")

        for i in range(self.num_filas):           # Recorre todas las filas (0 a num_filas-1)
            for j in range(self.num_columnas):    # Recorre todas las columnas (0 a num_columnas-1)
                self.matriz[i][j] = leer_float(f"Elemento [{i}][{j}]: ")

    def Mostrar(self):
        """
        Método para mostrar los elementos de la matriz.
        """
        if not self.Existe():
            print("La matriz no existe. Cree una matriz primero.")
            return
    
        print("Matriz:")
        print(self.matriz)
        
    def Existe(self):
        """
        Método que verifica si matriz está creada y no está vacía.
        Retorna True si existe, de lo contrario retorna False.
        """
        return self.matriz is not None and self.matriz.size > 0
    
    def SumarMatrices(self, otra_matriz):
        """
        Método que suma la matriz actual con otra matriz.
        Parámetros:
        otra_matriz: objeto de CMatFloat con la matriz a sumar.
        Retorna:
        numpy.ndarray: La matriz resultante de la suma.
        """
        #Nota: Las dimensiones de ambas matrices deben coincidir.
        if self.num_filas != otra_matriz.num_filas or self.num_columnas != otra_matriz.num_columnas:
            print("Error: Las dimensiones de las matrices no coinciden.")
            return None
        
        return self.matriz + otra_matriz.matriz  

    def RestarMatrices(self, otra_matriz):
        """
        Método que resta la matriz actual con otra matriz.
        Parámetros:
        otra_matriz: objeto de CMatFloat con la matriz a restar.
        Retorna:
        numpy.ndarray: La matriz resultante de la resta.
        """
        #Nota: Las dimensiones de ambas matrices deben coincidir.
        if self.num_filas != otra_matriz.num_filas or self.num_columnas != otra_matriz.num_columnas:
            print("Error: Las dimensiones de las matrices no coinciden.")
            return None
        
        return self.matriz - otra_matriz.matriz

#FUNCIONES AUXILIARES

def leer_int(mensaje="Introduce un número entero: "):
    """
    Función auxiliar que lee un número entero del teclado.
    Si se introduce un valor no válido, se solicita de nuevo.
    
    Parámetros:
    mensaje (str): El mensaje que se muestra al usuario
    solicitando la entrada.
    Retorna:
    int: El valor entero introducido por el usuario.
    """
    while True:
        try:
            valor = int(input(mensaje))
            return valor
        except ValueError:
            print("Error: Por favor, introduce un número entero válido.")

def leer_float(mensaje="Introduce un número decimal: "):
    """
    Función auxiliar que solicita al usuario un número decimal.
    Si se introduce un valor no válido, se solicitar de nuevo.
    Parámetros:
    mensaje (str): El mensaje que se muestra al usuario
    solicitando la entrada.
    Retorna:
    float: El valor decimal introducido por el usuario.
    """
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Por favor, introduce un número decimal válido.")


def crear_menu(opciones_menu):
    """
    Función que muestra un menú de opciones y solicita al usuario
    que seleccione una opción válida.
    Parámetros:
    opciones_menu (list): lista de opciones a mostrar en el
    menú.
    Retorna:
    int: El número de opción seleccionado por el usuario.
    """
    print("\n" + "="*50)
    print("MENÚ PRINCIPAL")
    print("="*50)
    
    for i, opcion in enumerate(opciones_menu, 1):
        print(f"{i}. {opcion}")
    
    print("="*50)
    
    while True:
        try:
            seleccion = int(input("Selecciona una opción: "))
            if 1 <= seleccion <= len(opciones_menu):
                return seleccion
            else:
                print(f"Error: Por favor, selecciona una opción entre 1 y {len(opciones_menu)}")
        except ValueError:
            print("Error: Por favor, introduce un número válido.")

def opciones_menu():
    """
    Función principal que gestiona el menú de operaciones con matrices.
    """
    matriz1 = CMatFloat()
    matriz2 = CMatFloat()
    
    opciones = [
        "Crear Matriz 1D",
        "Crear Matriz 2D",
        "Introducir elementos de la matriz",
        "Mostrar matriz",
        "Sumar dos matrices",
        "Restar dos matrices",
        "Salir"
    ]
    
    while True:
        opcion = crear_menu(opciones)
        match opcion:
            case 1:  # Crear Matriz 1D
                num_matriz = leer_int("¿Qué matriz deseas crear? (1 o 2): ")
                if num_matriz not in [1, 2]:
                    print("Error: Selecciona matriz 1 o 2.")
                    continue
                
                matriz = matriz1 if num_matriz == 1 else matriz2
                n_elementos = leer_int("Introduce el número de elementos: ")
                matriz.CrearMatriz1D(n_elementos)
                print(f"Matriz 1D de {n_elementos} elementos creada.")
            
            case 2:  # Crear Matriz 2D
                num_matriz = leer_int("¿Qué matriz deseas crear? (1 o 2): ")
                if num_matriz not in [1, 2]:
                    print("Error: Selecciona matriz 1 o 2.")
                    continue
                
                matriz = matriz1 if num_matriz == 1 else matriz2
                filas = leer_int("Introduce el número de filas: ")
                columnas = leer_int("Introduce el número de columnas: ")
                matriz.CrearMatriz2D(filas, columnas)
                print(f"Matriz 2D de {filas}x{columnas} creada.")
            
            case 3:  # Introducir elementos
                num_matriz = leer_int("¿Qué matriz deseas rellenar? (1 o 2): ")
                if num_matriz not in [1, 2]:
                    print("Error: Selecciona matriz 1 o 2.")
                    continue
                
                matriz = matriz1 if num_matriz == 1 else matriz2
                matriz.Introducir()
            
            case 4:  # Mostrar matriz
                num_matriz = leer_int("¿Qué matriz deseas mostrar? (1 o 2): ")
                if num_matriz not in [1, 2]:
                    print("Error: Selecciona matriz 1 o 2.")
                    continue
                
                matriz = matriz1 if num_matriz == 1 else matriz2
                matriz.Mostrar()
            
            case 5:  # Sumar matrices
                if not (matriz1.Existe() and matriz2.Existe()):
                    print("Error: Ambas matrices deben estar creadas.")
                    continue
                
                resultado = matriz1.SumarMatrices(matriz2)
                if resultado is not None:
                    print("Resultado de la suma:")
                    print(resultado)
            
            case 6:  # Restar matrices
                if not (matriz1.Existe() and matriz2.Existe()):
                    print("Error: Ambas matrices deben estar creadas.")
                    continue
                
                resultado = matriz1.RestarMatrices(matriz2)
                if resultado is not None:
                    print("Resultado de la resta (Matriz1 - Matriz2):")
                    print(resultado)
            
            case 7:  # Salir
                print("\n¡Hasta luego!")
                break
            
            case _:  # Opción no válida
                print("Opción no válida.")


if __name__ == "__main__":
    opciones_menu()