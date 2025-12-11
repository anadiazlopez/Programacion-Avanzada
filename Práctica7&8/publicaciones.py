class Publicacion:
    def __init__(self, titulo, autor, anio):
        self._titulo = titulo
        self._autor = autor
        self._anio = anio

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, valor):
        self._anio = valor

    def descripcion(self):
        return (f"  - Título: {self._titulo}\n"
        f"  - Autor: {self._autor}\n"
        f"  - Año: {self._anio}\n")


class Libro(Publicacion):
    def __init__(self, titulo, autor, anio, genero):
        super().__init__(titulo, autor, anio)
        self._genero = genero

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        self._genero = valor

    def descripcion(self):
        base = super().descripcion()
        return ("LIBRO\n" 
                f"\n{base}" 
                f"  - Género: {self._genero}")


class Revista(Publicacion):
    def __init__(self, titulo, autor, anio, num_edicion):
        super().__init__(titulo, autor, anio)
        self._num_edicion = num_edicion

    @property
    def num_edicion(self):
        return self._num_edicion

    @num_edicion.setter
    def num_edicion(self, valor):
        self._num_edicion = valor

    def descripcion(self):
        base = super().descripcion()
        return ("REVISTA\n"
                f"\n{base}"
                f"  - Edición: {self._num_edicion}")