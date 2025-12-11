class ErrorBiblioteca(Exception):
    def __init__(self, mensaje="Error en la biblioteca"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorArchivo(ErrorBiblioteca):
    def __init__(self, mensaje="Error relacionado con archivo"):
        super().__init__(mensaje)