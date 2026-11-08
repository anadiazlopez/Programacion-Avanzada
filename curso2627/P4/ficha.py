from time_management import Time

class Ficha:
    def __init__(self, nombre: str = "", edad: int = 0, nacio: Time = Time.from_string("12:00:00 AM")):
        self.nombre = nombre
        self.edad = edad
        self.nacio = nacio

    @property
    def nombre(self):
        return self._nombre

    @property
    def edad(self):
        return self._edad

    @property
    def nacio(self):
        return self._nacio

    @nombre.setter
    def nombre(self, valor):
        if not isinstance(valor, str):
            raise TypeError("\nEl nombre tiene que ser un texto.\n")
        self._nombre = valor

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int):
            raise TypeError("\nLa edad no es correcta, hay que introducir un número.\n")
        if valor < 0:
            raise ValueError("\nLa edad no puede ser menor que 0.\n")
        self._edad = valor

    @nacio.setter
    def nacio(self, valor):
        # Error especificado en Time
        self._nacio = valor
    
    def visualizar(self):
        print("\n", "=*" * 30)
        print(f"\n- Nombre: {self._nombre.title()}\n- Edad: {self._edad}\n- Hora de nacimiento: {self._nacio.hours:02d}:{self._nacio.minutes:02d}:{self._nacio.seconds:02d} {self._nacio.time_format}")


        


















