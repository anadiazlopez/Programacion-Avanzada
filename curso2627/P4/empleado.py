from ficha import Ficha

class Empleado(Ficha):
    def __init__(self, nombre, edad, nacio, categoria: str = "", antiguedad: int = 0):
        super().__init__(nombre, edad, nacio)
        self.categoria = categoria
        self.antiguedad = antiguedad

    @property
    def categoria(self):
        return self._categoria

    @property
    def antiguedad(self):
        return self._antiguedad

    @categoria.setter
    def categoria(self, valor): 
        if not isinstance(valor, str):
            raise TypeError("\nLa categoría debería ser un texto.\n")

        categorias = ["administrativo", "administrativa", "técnico", "tecnico", "técnica", "tecnica"]
        categoria = valor.lower().strip()
        for categ in categorias:
            if categ == categoria:
                self._categoria = categ.title()
                break
        else:
            raise ValueError("\nLa categoría debe ser administrativo/a o técnico/a.\n")

    @antiguedad.setter
    def antiguedad(self, valor):
        if not isinstance(valor, int): 
            raise TypeError("\nLa antigüedad no es correcta, hay que introducir un número.\n")
        if valor < 0:
            raise ValueError("\nLa antigüedad no puede ser menor que 0.\n")
        self._antiguedad = valor

    def visualizar(self):
        super().visualizar()
        if self._antiguedad == 0:
            print(f"- Categoria: {self._categoria}\n- Antigüedad: menos de un año")
        else:
            print(f"- Categoria: {self._categoria}\n- Antigüedad: {self._antiguedad}")