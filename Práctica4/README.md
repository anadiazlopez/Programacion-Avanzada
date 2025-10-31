1. ¿Cómo puedo programar la validación de entrada de datos numéricos en Python?

Para validar entradas numéricas uso un bucle while True con try-except. Capturo la excepción ValueError que se lanza cuando la conversión falla. Básicamente, intentas convertir el input a int o float, y si falla, capturas el error y vuelves a pedir el dato.

2. Utilización de numpy

NumPy está optimizado para cálculos matemáticos y es mucho más rápido que las listas. Además, puedes hacer operaciones entre matrices directamente con operadores como + o -, mientras que con listas tendrías que hacer bucles manuales. También tiene funciones útiles como np.zeros() para inicializar matrices.

3. ¿Hay alguna alternativa más corta if-elif-else?

El match-case hace el código más legible cuando tienes muchas opciones. Es el equivalente al switch de otros lenguajes. Para menús con muchas opciones es más limpio visualmente que una cadena larga de if-elif.

4. ¿Cómo se validan las dimensiones de matrices antes de sumarlas o restarlas?

Se comparan los atributos num_filas y num_columnas de ambas matrices. Si cualquiera de las dimensiones no coincide, se retorna None y se muestra un mensaje de error. Solo si ambas dimensiones son iguales se realiza la operación con NumPy.

5. ¿Cómo verificar que dos matrices sean compatibles para operaciones?

Verificas que ambas matrices existan primero (con Existe()), y luego comparas sus dimensiones. Para suma y resta necesitas dimensiones idénticas. Haces la comprobación con un if que evalúa filas y columnas usando or para detectar cualquier discrepancia.

6. ¿Para qué utilizo la clase CMat() en mis programas de Python?

Para crear y manejar matrices de manera sencilla dentro de mis programas. Gracias a esta clase, puedo generar matrices 1D o 2D con valores inicializados en cero y luego modificarlas según mis necesidades. Me resulta útil porque me permite realizar operaciones como sumar o restar matrices sin tener que escribir manualmente los cálculos con bucles.

7. Utilización de CMat()

Respuest más general: funciona como una estructura de datos bidimensional que organiza elementos en filas y columnas. Sirve para realizar operaciones matemáticas complejas de manera eficiente, como álgebra lineal, procesamiento de datos científicos, cálculos estadísticos y algoritmos de machine learning. Su implementación optimizada permite manejar grandes volúmenes de información numérica con alto rendimiento.
