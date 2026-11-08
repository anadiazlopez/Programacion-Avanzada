from ficha import Ficha
import re

class Cliente(Ficha):
    def __init__(self, nombre, edad, nacio, dni: str = ""):
            super().__init__(nombre, edad, nacio)
            self.dni = dni
    
    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, valor: str):
        patron = r"^\d{8}[A-Z]$"
        if re.match(patron, valor.upper()):
            self._dni = valor.upper()  
        else:
            raise ValueError("\nEl formato del DNI es incorrecto: debe tener 8 dígitos y una letra.\n")

    def visualizar(self):
        super().visualizar()
        print(f"- DNI: {self._dni}")

    def __eq__(self, otro):
        if isinstance(otro, Cliente):
            return self.nombre.lower() == otro.nombre.lower() and self.edad == otro.edad
        return False
