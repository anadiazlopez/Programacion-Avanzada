Práctica 1&2- Preguntas realizadas a una LLM

GIT Ana Díaz López

1. ¿No hace falta que ponga de que tipo es la variable en Python para crearla (como en C)? (Claude)

En Python no necesito declarar el tipo de variable como en C. Simplemente asigno un valor y Python automáticamente detecta si es un número, texto u otro tipo. Esto también significa que debo tener más cuidado con los errores de tipo que en C el compilador detectaría automáticamente. Poner el tipo sirve principalmente para hacer el código más entendible, tanto para mí como para otros programadores que lo lean después.

2. ¿Cómo puedo escribir varias variables en una misma línea de código en Python, por ejemplo, cuando quiero imprimir varias palabras dentro de un bucle? (ChatGPT)

Para escribir varias variables en una misma línea de código en Python, por ejemplo cuando quiero imprimir varias palabras dentro de un bucle, hay wue usar el parámetro end en la función print(). Este parámetro evita que se haga un salto de línea después de cada impresión. Por ejemplo, si tengo una lista de palabras y hago:
  for palabra in palabras:
    print(palabra, end=" ")
todas se muestran en la misma línea, separadas por un espacio. De esta forma puedo controlar cómo se imprimen los valores sin que cada uno aparezca en una línea distinta.

3. (Similar a la pregunta 2.) Enséñame alguna manera o función en la que pueda mostrar por pantalla, una lista de variables sin que haya salto de línea. (ChatGPT)

En este caso, me ha ofrecido cuatro opciones o soluciones posibles. Puedo mostrar variables sin salto de línea en de varias formas: uso print() con el parámetro end para evitar el salto, convierto los valores a texto y los uno con join(), escribo directamente con sys.stdout.write(), o utilizo print(..., end=" ") dentro de un bucle para imprimir todo en la misma línea.

4. ¿Puedo usar una variable en un for sin declararla antes? (Claude)

Me surgió esta pregunta porque introduje sin querer una variable inexistente (mal escrita) y no dio error. Sí, en Python la variable del for se crea automáticamente al ejecutar el bucle. Cuando escribo for i in range(10):, Python genera la variable i en ese momento sin necesidad de declararla antes. Por eso no te dio error: Python simplemente creó la variable y la usó para iterar.

5. ¿Cómo introduzco una frase por teclado? (Claude)

Al ser la primera pregunta que he hecho hoy y no haber concretado el lenguaje de programación, el resultado han sido varias opciones: En Python, para introducir una frase por teclado, uso la función input() escribiendo frase = input("Escribe algo: "). En Java utilizo la clase Scanner con el método nextLine() para capturar toda la línea. En C++ empleo getline(cin, frase) para leer la frase completa incluyendo espacios. Por último, en C uso fgets() especificando el tamaño del buffer donde guardaré la entrada del usuario.

6. ¿Para que sirve el operador is? ¿Se puede usar ==? (ChatGPT)

El operador is en Python lo uso para saber si dos variables son el mismo objeto en memoria, no solo si tienen el mismo valor. Por ejemplo, a is b es True solo si ambas apuntan al mismo objeto. También lo uso para comprobar si algo es None, como en if x is None:.
La diferencia con == es que == compara los valores (si dos objetos tienen el mismo contenido), mientras que is compara la identidad (si son exactamente el mismo objeto en memoria).

7. ¿Qué son las funciones regulares re? (Claude)

Yo he entendido que las funciones regulares son funciones de Python que sirven para buscar y trabajar con textos usando patrones, como varias fechas en un texto, que siguen un patrón número/número/número. Las más importantes son re.compile() para crear el patrón, re.search() para buscar, re.findall() para encontrar todas las coincidencias y re.sub() para reemplazar texto.
