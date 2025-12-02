from time_management import Time

class Ficha:
    def __init__(self, nombre="", edad=0):
        self._nombre = nombre
        self._edad = edad
        self._nacio = Time()  

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        self._nombre = valor
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, valor):
        self._edad = valor
    
    @property
    def nacio(self):
        return self._nacio
    
    @nacio.setter
    def nacio(self, valor):
        self._nacio = valor
    
    def visualizar(self):
        print(f"\n  - Nombre: {self._nombre}")
        print(f"    - Edad: {self._edad}")
        print(f"    - Hora de nacimiento: {self._nacio}")


class Empleado(Ficha):
    def __init__(self, nombre="", edad=0, categoria="", antiguedad=0):
        super().__init__(nombre, edad)
        self._categoria = categoria
        self._antiguedad = antiguedad

    @property
    def categoria(self):
        return self._categoria
    
    @categoria.setter
    def categoria(self, valor):
        self._categoria = valor
    
    @property
    def antiguedad(self):
        return self._antiguedad
    
    @antiguedad.setter
    def antiguedad(self, valor):
        self._antiguedad = valor

    def visualizar(self):
        super().visualizar()
        print(f"    - Categoría: {self._categoria}")
        print(f"    - Antigüedad: {self._antiguedad} años")


class Cliente(Ficha):
    def __init__(self, nombre="", edad=0, dni=""):
        super().__init__(nombre, edad)
        self._dni = dni
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, valor):
        self._dni = valor
    
    def visualizar(self):
        super().visualizar()
        print(f"    - DNI: {self._dni}")

    def __eq__(self, otro):
        if isinstance(otro, Cliente):
            return self._nombre == otro._nombre and self._edad == otro._edad
        return False


class RegistroDiario:
    def __init__(self):
        self._personas = []
    
    def agregar_persona(self, persona):
        if isinstance(persona, (Empleado, Cliente)):
            self._personas.append(persona)
            return True
        return False
    
    def visualizar_registro(self):
        for persona in self._personas:
            persona.visualizar()
    
    def visualizar_empleados(self):
        for persona in self._personas:
            if isinstance(persona, Empleado):
                persona.visualizar()
    
    def es_empleado(self, persona):
        return isinstance(persona, Empleado)
    
    def __getitem__(self, index):
        if 0 <= index < len(self._personas):
            return self._personas[index]
        raise IndexError(f"Índice {index} fuera de rango")
    
    def __add__(self, otro_registro):
        if not isinstance(otro_registro, RegistroDiario):
            raise TypeError("Solo se pueden sumar RegistroDiario con RegistroDiario")
        
        nuevo_registro = RegistroDiario()
        nuevo_registro._personas = self._personas + otro_registro._personas
        return nuevo_registro
    
    def buscar_por_nombre_edad(self, nombre, edad):
        resultados = []
        for persona in self._personas:
            if persona.nombre == nombre and persona.edad == edad:
                resultados.append(persona)
        return resultados
    
    def __len__(self):
        return len(self._personas)