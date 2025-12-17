import json

ARCHIVO_DATOS = r"C:\Users\anadi\Desktop\uni\2025-2026\PRIMER CUATRIMESTRE\PROGRAMACIÓN AVANZADA\estudio PRL- PROGRA\coches.json"

class Coche:
    def __init__(self, matricula, marca, ano, km, gastos):
        self._matricula = matricula
        self._marca = marca
        self._ano = ano
        self._km = km
        self._gastos = gastos

    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula
    
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self, marca):
        self._marca = marca
    
    @property
    def ano(self):
        return self._ano
    
    @ano.setter
    def ano(self, ano):
        self._ano = ano

    @property
    def km(self):
        return self._km
    
    @km.setter
    def km(self, km):
        self._km = km

    @property
    def gastos(self):
        return self._gastos
    
    @gastos.setter
    def gastos(self, gastos):
        self._gastos += gastos

    def mostrar(self):
        return(f"\nInformación del vehículo {self._matricula}:"
              f"\n{self._marca} ({self._ano}) - {self._km} km"
              f"\nTotal gastos revisiones: {self._gastos} €")


class Taller:
    def __init__(self):
        self.coches = []
        self._total_km = 0      
        self._total_gastos = 0  
    
    def agregar_coche(self, coche):
        self.coches.append(coche)
        self._total_km += coche.km        
        self._total_gastos += coche.gastos 
    
    def mostrar(self):
        num = len(self.coches)
        promedio = self._total_km / num if num > 0 else 0
        
        return (f"\nEstadísticas:"
                f"\n    - Total vehículos: {num}"
                f"\n    - Kilometraje promedio: {int(promedio)} km"
                f"\n    - Total gastos en revisiones: {self._total_gastos:.2f} €")
    

class ErrorTaller(Exception):
    def __init__(self, mensaje="\nError en el taller."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorCocheDuplicado(ErrorTaller):
    def __init__(self, mensaje="\nError: coche duplicado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorFechaInvalida(ErrorTaller):
    def __init__(self, mensaje="\nError: fecha inferior a 1990."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Datos de ejemplo
lista_coches_ejemplo = [
    ("DET564", "Fiat 500", 2020, 200190, 256.99),
    ("AJA834", "Audi A3", 2023, 80050, 489.50),
    ("RTU290", "Ford Fiesta", 1971, 300500, 234.95),
    ("RPS002", "Seat Ibiza", 2017, 110000, 115.15),
    ("DYE853", "BMW x6", 2025, 10000, 506.78),
]

def cargar_coches_iniciales(taller):
    """Carga los coches de ejemplo al iniciar"""
    for datos in lista_coches_ejemplo:
        coche = Coche(*datos)
        taller.agregar_coche(coche)

def mostrar_coches(taller):
    if len(taller.coches) == 0:
        print("No hay coches en el taller.")
        return
    
    print("\n=== LISTA DE COCHES ===")
    for coche in taller.coches:
        print(coche.mostrar())

def mostrar_estadisticas(taller):
    print(taller.mostrar())

def anadir_coche(taller):
    try:
        matricula = input("Inserte la matrícula de su coche: ").strip().upper()
        if len(matricula) != 6:
            raise ValueError("La matrícula tiene que tener 6 caracteres únicamente.")
        for coche in taller.coches:
            if coche.matricula == matricula:
                raise ErrorCocheDuplicado(matricula)
        marca = input("Inserte la marca: ").strip()
        ano = int(input("¿En qué año se matriculó?: "))
        if ano < 1990:
            raise ErrorFechaInvalida() 
        km = int(input("Kilómetros actuales: "))
        if km < 0:
            raise ValueError("Los kilómetros no pueden ser negativos")
        gastos = float(input("Ingrese precio a pagar: "))
        if gastos < 0:
            raise ValueError("\nEl precio no puede ser negativo")
        
        nuevo_coche = Coche(matricula, marca, ano, km, gastos)
        taller.agregar_coche(nuevo_coche)
        print(f"Coche con matrícula {matricula} añadido correctamente.")
         
    except ErrorFechaInvalida as e:
        print(e)
    except ErrorCocheDuplicado as e:
        print(e)
    except ValueError as e:
        print(f"\nError: {e}")

def guardar_datos(taller):
    try:
        datos = []
        for coche in taller.coches:
            datos.append({
                "matricula": coche._matricula,
                "marca": coche._marca,
                "ano": coche._ano,
                "km": coche._km,
                "gastos": coche._gastos
            })
        
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2)
        
        print(f"Datos guardados en: {ARCHIVO_DATOS}")

    except Exception as e:
        print(f"Error al guardar: {e}")

def cargar_datos(taller):
    try:
        # Intentar abrir el archivo
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as f:
            datos = json.load(f)
        
        # Limpiar datos actuales del taller
        taller.coches.clear()
        taller._total_km = 0
        taller._total_gastos = 0
        
        # Cargar nuevos datos
        for item in datos:
            coche = Coche(
                item["matricula"],
                item["marca"],
                item["ano"],
                item["km"],
                item["gastos"]
            )
            taller.agregar_coche(coche)
        
        print(f"Datos cargados desde: {ARCHIVO_DATOS}")
        print(f"Total de coches cargados: {len(taller.coches)}")
        
    except FileNotFoundError:
        print(f"Archivo no encontrado: {ARCHIVO_DATOS}")
        print("Se trabajará con datos vacíos.")
    except json.JSONDecodeError:
        print(f"Error: El archivo {ARCHIVO_DATOS} está corrupto o vacío")
        print("Se trabajará con datos vacíos.")
    except Exception as e:
        print(f"Error al cargar: {e}")

def main():
    taller = Taller()
    
    # Cargar datos iniciales (ejemplo)
    cargar_coches_iniciales(taller)
    
    while True:
        print("\n" + "="*40)
        print("SISTEMA DE GESTIÓN DEL TALLER")
        print("="*40)
        print("1. Mostrar todos los coches")
        print("2. Mostrar estadísticas")
        print("3. Añadir coche nuevo")
        print("4. Guardar datos en archivo")
        print("5. Cargar datos desde archivo")
        print("6. Salir")
        print("="*40)
        
        opcion = input("\nSelecciona opción: ").strip()

        if opcion == "1":
            mostrar_coches(taller)
            
        elif opcion == "2":
            mostrar_estadisticas(taller)

        elif opcion == "3":
            anadir_coche(taller)

        elif opcion == "4":
            guardar_datos(taller)

        elif opcion == "5":
            cargar_datos(taller)

        elif opcion == "6":
            print("\n¿Desea guardar los datos antes de salir? (s/n): ", end="")
            guardar_salir = input().strip().lower()
            if guardar_salir == 's':
                guardar_datos(taller)
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()