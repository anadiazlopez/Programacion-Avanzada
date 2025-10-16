import re                                       # Importa el módulo 're' para trabajar con expresiones regulares

class Time:                                     # Define una clase llamada Time para manejar tiempos
    TIME_FORMATS = ("AM", "PM", "24 HOURS")     # Formatos válidos de tiempo
    time_count = 0                              # Variable de clase para contar cuántos objetos Time se han creado
    
    def __init__(self):                         # Constructor de la clase
        self.hours = 0                          
        self.minutes = 0                        
        self.seconds = 0                        
        self.format = "24 HOURS"  

    def __asign_format(self, pszFormat):        # Método privado para asignar formato
        fmt = pszFormat.upper()                 # Convierte el formato a mayúsculas para comparar

        if fmt in Time.TIME_FORMATS:            # Verifica si el formato es válido
            self.format = fmt                   # Asigna el formato si es válido
            return True                         
        else:
            return False                  

    def __is_24hour_format(self):               # Método privado para saber si el formato es de 24 horas
        return self.format == "24 HOURS"        

    def _is_valid_time(self):                   # Método protegido para validar horas, minutos y segundos
        if not (0 <= self.minutes <= 59 and 0 <= self.seconds <= 59):  
            return False
        return (0 <= self.hours <= 23) if self.__is_24hour_format() else (1 <= self.hours <= 12)

    def set_time(self, nHours, nMins, nSec, pszFormat):     # Método público para establecer la hora
        if not self.__asign_format(pszFormat):              # Verifica si el formato ingresado es válido
            print(f"Formato inválido '{pszFormat}'.")
            return False
        
        self.hours = nHours     
        self.minutes = nMins   
        self.seconds = nSec     

        if not self._is_valid_time():                       # Valida si la hora establecida es correcta
            print("Valores de tiempo inválidos.")
            self.hours = 0            
            self.minutes = 0        
            self.seconds = 0          
            self.format = "24 HOURS"  
            return False
        return True  

    def get_time(self):                                     # Método público para obtener la hora como diccionario
        return {
            'hours': self.hours,
            'minutes': self.minutes,
            'seconds': self.seconds,
            'format': self.format
        }

    @classmethod  # Decorador de método de clase
    def from_string(cls, time_string):          # Crea un objeto Time desde una cadena de texto
        pattern = r'^(\d{1,2}):(\d{1,2}):(\d{1,2})\s+(AM|PM|24 HOURS)$'     # Expresión regular para validar formato de tiempo
        
        match = re.match(pattern, time_string.strip(), re.IGNORECASE)       # Busca coincidencias con la expresión regular
        
        if match:  # Si hay coincidencia con la expresión
            hours = int(match.group(1))                                     # Extrae y convierte las horas
            minutes = int(match.group(2))                                   # Extrae y convierte los minutos
            seconds = int(match.group(3))                                   # Extrae y convierte los segundos
            time_format = match.group(4).upper()                            # Extrae y convierte el formato a mayúsculas
            new_time = cls()                                                # Crea un nuevo objeto Time
            if new_time.set_time(hours, minutes, seconds, time_format):     # Intenta establecer la hora
                return new_time                                             # Devuelve el nuevo objeto si es válido
            else:
                return None                                                 # Devuelve None si no es válido
        else:
            print("Error: Formato de cadena de tiempo inválido.")
            print("Formato esperado: 'HH:MM:SS FORMAT' (ej: '14:30:00 24 HOURS' o '02:30:00 PM')")
            return None
        
    @staticmethod                                                           # Decorador de método estático
    def is_valid_format(time_format):                                       # Verifica si un formato es válido sin necesidad de crear objeto
        return time_format.upper() in Time.TIME_FORMATS                     # Devuelve True si es un formato válido
    
    @classmethod
    def get_time_count(cls):                                                # Devuelve cuántos objetos Time se han creado
        return cls.time_count

def show_menu():                                                            # Función que muestra el menú de opciones en pantalla
    print("\nSISTEMA DE GESTIÓN DE TIEMPO\n")
    print("1. Introducir una nueva hora")
    print("2. Visualizar hora")
    print("3. Crear una hora a partir de una cadena")
    print("4. Terminar\n")
    

def input_new_time(time_obj):                                               # Función para ingresar una nueva hora manualmente
    print("\nIntroducir nueva hora")
    try:
        hours = int(input("Ingrese las horas: "))    
        minutes = int(input("Ingrese los minutos: "))
        seconds = int(input("Ingrese los segundos: "))
        
        print("\nFormatos disponibles: AM, PM, 24 HOURS")
        time_format = input("Ingrese el formato: ").strip()                 # Pide el formato
        
        if time_obj.set_time(hours, minutes, seconds, time_format):         # Intenta establecer la hora
            print("\nHora establecida correctamente.")
            display_time(time_obj)                                          # Muestra la hora si fue correcta

    except ValueError:
        print("\nError: Debe ingresar valores numéricos para horas, minutos y segundos.")  

def display_time(time_obj):                                                 
    print("\nHORA ACTUAL\n")
    time_data = time_obj.get_time()                                         # Obtiene la hora del objeto
    print(f"Hora: {time_data['hours']:02d}:{time_data['minutes']:02d}:{time_data['seconds']:02d} {time_data['format']}\n")

def main():         
    time = Time()                                                   # Crea un objeto Time inicial
    
    print("\n¡Bienvenido al Sistema de Gestión de Tiempo!")
    print(f"Objetos Time creados: {Time.get_time_count()}")                 # Muestra cuántos objetos se han creado
    
    while True: 
        show_menu()  
        option = input("\nSeleccione una opción (1-4): ").strip()           # Pide opción al usuario
            
        if option == '1':  
            input_new_time(time)
        elif option == '2':  
            display_time(time)
        elif option == '3':  
            print("\n--- Crear hora desde cadena ---")
            print("Formato esperado: 'HH:MM:SS FORMAT'")
            print("Ejemplos: '14:30:00 24 HOURS', '02:30:00 PM', '11:45:30 AM'")
                
            time_string = input("\nIngrese la cadena de tiempo: ").strip()  
                
            time2 = Time.from_string(time_string)                        # Intenta crear un nuevo objeto desde la cadena
                
            if time2:                                                    # Si fue exitoso
                time = time2
                print("\nHora creada correctamente desde la cadena.")
                display_time(time)
                print(f"Total de objetos Time creados: {Time.get_time_count()}")
        elif option == '4':  
            print("\n¡Gracias por usar el Sistema de Gestión de Tiempo!")
            print(f"Total de objetos Time creados durante la sesión: {Time.get_time_count()}")
            print("¡Hasta luego!\n")
            break  # Sale del bucle
        else:
            print("\nError: Opción inválida. Por favor seleccione un número entre 1 y 4.")
                
    
if __name__ == "__main__":                              
    main()  
