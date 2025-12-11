import pickle
from excepciones import ErrorArchivo

def validar_titulo(titulo):
    if not titulo or titulo.strip() == "":
        raise ValueError("El título no puede estar vacío.")

def validar_anio(anio):
    try:
        anio_int = int(anio)
        if anio_int <= 0:
            raise ValueError("El año debe ser un entero positivo.")
    except ValueError:
        raise ValueError("El año debe ser un número entero.")

def guardar_publicaciones(publicaciones, nombre_archivo):
    try:
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(publicaciones, archivo)
        print(f"Publicaciones guardadas en '{nombre_archivo}'.")
    except Exception as e:
        raise ErrorArchivo(f"No se pudo guardar el archivo: {e}.")

def cargar_publicaciones(nombre_archivo):
    try:
        with open(nombre_archivo, 'rb') as archivo:
            publicaciones = pickle.load(archivo)
        print(f"Publicaciones cargadas desde '{nombre_archivo}.'")
        return publicaciones
    except FileNotFoundError:
        raise ErrorArchivo("El archivo no existe.")
    except EOFError:
        raise ErrorArchivo("El archivo está vacío o corrupto.")
    except Exception as e:
        raise ErrorArchivo(f"No se pudo cargar el archivo: {e}.")