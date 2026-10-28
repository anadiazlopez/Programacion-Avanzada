PRÁCTICA 6- Ana Díaz López

1. ¿Para qué necesito realmente el eq en Cliente?

Para comparar directamente si dos clientes son iguales. Cuando haces cliente1 == cliente2, Python usa ese método para compararlos por nombre y edad.

2. ¿CQué pasa si no pongo super().init() en Empleado?

La clase Empleado no inicializaría nombre, edad y nacio. Quedarían como atributos no definidos. Super() llama al constructor de Ficha para que haga su parte, luego Empleado añade categoría y antigüedad.

3. Si los atributos son privados (_nombre), ¿por qué no hacerlos públicos y ahorrarme los getters/setters?

El encapsulamiento protege la integridad de los datos. Si _edad es público, cualquiera podría poner persona.edad = -10. Con @property, el setter se puede validar que la edad sea positiva. Además, si cambio cómo almaceno la edad, el código externo sigue viendo .edad igual.

4. ¿No sería más simple una sola clase Persona con todos los atributos posibles?

Parece más simple al principio, pero se vuelve complicado. Tendría atributos como categoria y dni en la misma clase, cuando no tienen sentido juntos. Con herencia, Empleado tiene lo que necesita, Cliente tiene lo suyo, y el código es más claro. Además, se evitan muchos if tipo == "empleado" en mi código.

5. ¿Es mejor validar todo antes (como en leer_entero) o capturar excepciones después (try-except)?

En leer_entero() se valida desde el principio que el dato sea correcto. Los try-except se usan para errores imprevistos (como índice fuera de rango).

6. ¿Por qué algunos métodos como agregar_persona devuelven True o False?

Para informar si la operación tuvo éxito. Si intento agregar algo que no es Empleado ni Cliente, devuelve False y el programa puede rmostrar error. 

7. He mostado el error ModuleNotFoundError: No module named 'time_management'

Identificó que el archivo no estaba en el mismo directorio o Python no lo encontraba. Tenía que copiar el archivo a la misma carpeta (luego fue modificado).


















