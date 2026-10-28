Práctica 5- Ana Díaz López

1. ¿Cómo puedo poner una palabra random entre varias opciones en Python?

Para seleccionar una palabra aleatoria entre varias opciones, la forma más directa es utilizando la función random.choice() del módulo random. 
  import random
  libro.estado = random.choice(["Disponible", "Prestado"])

2. ¿Por qué necesito usar el decorador @property en mis atributos privados en lugar de hacerlos públicos directamente?

Se usa @property porque me permite mantener el encapsulamiento de mis clases. Cuando declaro atributos como _nombre o _id como privados y luego creo properties, estoy protegiendo los datos internos de mi clase.

3. ¿Cuál es la diferencia práctica entre usar enumerate() en un bucle for y no usarlo?

enumerate() sirve para cuando necesito saber la posición (índice) de cada elemento mientras recorro una lista. Sin enumerate() solo obtengo el elemento for libro in libros:, y con enumerate() obtengo tanto el índice como el elemento for i, libro in enumerate(libros):

4. ¿Por qué a veces me aparece el error "function object is not iterable" y cómo lo soluciono?
   
Este error sale cuando uso una función sin paréntesis, como lista_libros en lugar de lista_libros(). Sin los paréntesis, Python ve la función como un objeto, no como el resultado que devuelve. 

5. ¿Por qué necesito un decorador si puedo poner los prints directamente en la función?

Al principio pensé que era más fácil poner los prints directamente en la función, pero el decorador me permite separar la lógica de la operación del sistema de registro. Así si necesito cambiar cómo se registran las operaciones, solo modifico el decorador una vez y todas las funciones decoradas se actualizan automáticamente, haciendo mi código más organizado y reutilizable.

6. ¿Por qué a veces mis métodos de la clase no reconocen los atributos y me da error de que no están definidos?

Este error me pasa cuando uso biblioteca.mostrar_libros() en lugar de self.mostrar_libros() dentro de los métodos de mi clase. Debo usar self para acceder a los atributos y métodos de la misma instancia, no el nombre de la variable que uso fuera de la clase.

7. ¿Por qué debo usar functools.wraps si mi programa funciona sin él?

Mi programa funciona sin functools.wraps, pero este preserva el nombre y documentación original de la función. Sin él, al inspeccionar mi función decorada vería "wrapper" en lugar de "math_operation", lo que podría causar confusión. 
