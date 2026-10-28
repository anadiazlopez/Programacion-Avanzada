import re

class Time:
    """
    Clase que representa una hora en formato AM/PM o 24 horas.
    Atributos de clase:
        TIME_FORMATS # p. ej.: "AM", "PM", "24 HOURS"
        time_count = 0 # Cuenta el número de objetos Time creados
    Atributos:
        # Los atributos deben ser privados y exponerse mediante
        # property
        hours # Guarda las horas
        # (1 a 12 en AM/PM, 0 a 23 en 24 HOURS)
        minutes # Guarda los minutos (0 a 59)
        seconds # Guarda los segundos (0 a 59)
        time_format # Guarda el formato: "AM", "PM" o "24 HOURS"
    """

    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0

    def __init__(self, *args, **kwargs):
        """
        Inicializa los atributos a 0.
        Es el único método que se le pasa parámetros como ejemplo
        """
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        self.__time_format = "24 HOURS"

        Time.time_count += 1

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    @property
    def time_format(self):
        return self.__time_format

    def __assign_format(self, time_format):
        """
        Comprueba que time_format tiene un valor correcto y lo
        asigna al atributo correspondiente.
        Lo convierte a mayúsculas para evitar problemas de
        capitalización.
        Args:
            time_format: cadena con el formato de hora
            ("AM", "PM" o "24 HOURS").
        Devuelve:
            True si el formato es correcto, False en caso
            contrario.
        """
        time_format =  time_format.upper()

        if time_format in Time.TIME_FORMATS:
            self.__time_format = time_format
            return True
        return False

    def __is_24hour_format(self):
        """
        Comprueba si el formato de la hora es "24 HOURS".
        Devuelve:
            True si formato es "24 HOURS", False en caso contrario.
        """
        return self.__time_format == "24 HOURS"

    def _is_valid_time(self):
        """
        Comprueba si la hora es correcta según el formato.
        Devuelve:
            True si la hora es correcta, False en caso contrario.
        """
        if not (0 <= self.__minutes <= 59 and 0 <= self.__seconds <= 59):
            return False

        if self.__is_24hour_format():
            return 0 <= self.__hours <= 23
        return 1 <= self.__hours <= 12      

    def set_time(self, *args, **kwargs):
        """
        Asigna una hora.

        Devuélve la instancia
        # Muestre mensaje si el formato de la cadena no es válido
        """
        horas= args[0] if len(args) > 0 else kwargs.get("hours", self.__hours)
        mins = args[1] if len(args) > 1 else kwargs.get("minutes", self.__minutes)
        segs = args[2] if len(args) > 2 else kwargs.get("seconds", self.__seconds)
        formt = args[3] if len(args) > 3 else kwargs.get("time_format", self.__time_format)

        if not self.__assign_format(formt):
            print("Error: El formato de hora no es válido.")
            return self

        # Guardar valores actuales por si la hora falla
        h, m, s = self.__hours, self.__minutes, self.__seconds
        self.__hours, self.__minutes, self.__seconds = horas, mins, segs

        # Validar la hora y si no es válida, se escribe la anterior
        if not self._is_valid_time():
            print("\nError: La hora introducida no es válida.")
            self.__hours, self.__minutes, self.__seconds = h, m, s
        return self

    def is_valid_format(self, time_format):
        """
        Comprueba si un formato de hora dado es válido.
        Args:
            time_format: cadena con el formato de hora a comprobar.
        Devuelve:
            True si el formato es válido (AM, PM o 24 HOURS),
            False en caso contrario.
        """
        return time_format.upper() in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        """
        Devuelve el número de objetos de la clase que se han
        creado.
        Devuelve:
            Un número entero de objetos Time creados.
        """
        return cls.time_count

def introducir():
    horas = int(input("Escribe la hora: "))
    minutos = int(input("Escribe los minutos: "))
    segundos = int(input("Escribe los segundos: "))
    formato = input("Escribe el formato (AM, PM o 24 HOURS): ")

    return Time().set_time(horas, minutos, segundos, formato)


def visualizar(tiempo):
    print(f"\n{tiempo.hours:02}:{tiempo.minutes:02}:{tiempo.seconds:02} {tiempo.time_format}")


def crear():
    cadena = input("Escribe la hora (“HH:MM:SS FORMATO”): ")
    exp = r"^(\d{2}):(\d{2}):(\d{2})\s+(AM|PM|24\s+HOURS)$"

    coincide = re.match(exp, cadena.upper())

    if coincide:
        h, m, s, fmt = coincide.groups()
        return Time().set_time(int(h), int(m), int(s), fmt)
    else:
        print("\nError: El formato de la cadena no es válido.")
        return None


def menu():
    print("\n\n1. Introducir una nueva hora.")
    print("2. Visualizar hora.")
    print("3. Crear una hora a partir de una cadena.")
    print("4. Salir.")

    return input("\nSelecciona una opción (1 - 4): ").strip()


def main():
    tiempo = None

    while True:
        opcion = menu()

        if opcion == "1":
            tiempo = introducir()
        elif opcion == "2":
            if tiempo:
                visualizar(tiempo)
            else:
                print("\nNo hay ninguna hora introducida.")
        elif opcion == "3":
            tiempo = crear() 
        elif opcion == "4":
            print(f"Horas creadas: {Time.get_time_count()}")
            print("Saliendo...")
            break
        else:
            print("El dato introducido es erróneo. Vuelve a intentarlo.")


if __name__ == "__main__":
    main()
 