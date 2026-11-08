from empleado import Empleado
from cliente import Cliente
from ficha import Ficha

class RegistroDiario:
    def __init__(self):
        self._personas = []

    @property
    def personas(self):
        return self._personas

    @personas.setter
    def personas(self, valor: list[Ficha]):
        if not isinstance(valor, list):
            raise TypeError("\nEl valor debe ser una lista de personas.\n")
        self._personas = valor

    def agregar_persona(self, persona):
        self._personas.append(persona)

    def visualizar_registro(self):
        for persona in self._personas:
            persona.visualizar()
        print("\n", "=*" * 30)

        if not self._personas:
            print("\nRegistro vacío.\n")

    def visualizar_empleados(self):
        contador = 0
        for persona in self._personas:
            if self.es_empleado(persona):
                persona.visualizar()
                contador += 1
        print("\n", "=*" * 30)
        
        if contador == 0:
            print("\nNo hay ningún empleado registrado.\n")

    def es_empleado(self, persona):
        return isinstance(persona, Empleado)

    def __getitem__(self, key):
        return self._personas[key]

    def __add__(self, otro_registro:"RegistroDiario"):
        nuevo_registro = RegistroDiario()
        for persona in self._personas:
            nuevo_registro.agregar_persona(persona)
        if isinstance(otro_registro, RegistroDiario):
            for persona in otro_registro.personas:
                nuevo_registro.agregar_persona(persona)
        return nuevo_registro

