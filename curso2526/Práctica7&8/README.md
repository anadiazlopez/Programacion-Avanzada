Práctica 7 y 8: Ana Díaz López

- ¿Por qué en la función cargar() necesito escribir "global publicaciones" pero en las otras funciones no?
  
Porque en cargar() se está reasignando la variable publicaciones (con =), mientras que en otras solo se modifica su contenido (con .append()), y Python necesita saber que es global para reasignarla.

- ¿Cómo hago para que al añadir una revista, no acepte números de edición como "3.5" o "tres"?

Esto lo hace .isdigit() en la validación de números, que solo acepta strings compuestos exclusivamente por dígitos (0-9), rechazando decimales y texto.

- ¿Por qué creo una excepción personalizada ErrorBiblioteca que hereda de Exception en lugar de usar las estándar?
  
Para tener errores específicos de mi dominio que sean más descriptivos y fáciles de capturar selectivamente, diferenciando errores de biblioteca de otros errores del sistema.

- En la opción de añadir revistas, ¿por qué uso .isdigit() para validar un número en lugar de try/except como con el año?
  
Porque isdigit() es más específico para strings que deben ser números enteros positivos, mientras que int() convertiría "-5" que no debería ser válido para edición.

- ¿Qué ocurriría si guardo publicaciones, cierro el programa, y al volver a abrirlo intento cargar sin haber añadido nuevas publicaciones?
  
La lista publicaciones estaría vacía y cargar() la reemplazaría con lo del archivo; pero si no especifico archivo o no existe, mantendría vacía sin mostrar error.

- ¿Por qué mi implementación de guardar_publicaciones() en Utils.py usa modo 'wb' (write binary) en lugar de 'w' (write text) para pickle?

Porque pickle serializa objetos a bytes binarios, no texto. El modo 'wb' garantiza que los bytes se escriban correctamente sin conversiones de caracteres que corromperían los datos.

- ¿Cómo hago para que si guardo en un archivo y luego intento cargar un archivo que no existe, el programa me diga "Archivo no encontrado" en lugar de dar error feo?

En Utils.py con except FileNotFoundError:, pero si no se muestra, verifica que en main.py estés capturando ErrorBiblioteca y no otro tipo de excepción.
