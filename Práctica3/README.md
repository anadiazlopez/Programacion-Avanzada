Práctica 3

GIT Ana Díaz López

1. ¿Por qué es necesario importar el módulo re en mi programa?

El módulo re es esencial porque permite trabajar con expresiones regulares. Gracias a eso pude validar que las cadenas que ingresan los usuarios tengan el formato correcto de hora. Sin ese módulo, hubiera tenido que hacer validaciones manuales mucho más largas y propensas a errores.

2. ¿Cuál es la ventaja de usar atributos de clase como TIME_FORMATS y time_count en lugar de atributos de instancia?
    
Entendí que TIME_FORMATS y time_count tienen sentido como atributos de clase porque su valor es común para todas las instancias. No cambia de un objeto a otro, y eso evita duplicar información innecesariamente. Además, time_count me permite llevar un control global de cuántos objetos Time he creado.

3. ¿Para qué sirve exactamente el método from_string?

El método from_string me facilita crear un objeto Time de manera directa a partir de un texto. Esto hace que el programa sea más práctico, ya que no necesito pedir cada valor por separado. También me permite validar la cadena completa de forma automática usando expresiones regulares.

4. ¿Por qué algunos métodos tienen doble guion bajo al inicio de su nombre?

Resulta que el doble guion bajo indica que un método es “privado” dentro de la clase. No es que sea completamente inaccesible, pero sugiere que no debería ser usado fuera de la propia clase. Esto me ayuda a mantener mi código más organizado y a proteger la lógica interna de modificaciones accidentales.

5. ¿Qué beneficio obtengo al separar la lógica en funciones como show_menu, input_new_time o display_time?

Separar la lógica en funciones hace que el código sea más claro, reutilizable y fácil de mantener. Si necesito cambiar la forma en que se muestra la hora, por ejemplo, solo tengo que modificar display_time sin tocar el resto del programa.

6. ¿Por qué es útil usar expresiones regulares en lugar de simples condicionales para validar la hora?

Las expresiones regulares simplifican mucho la validación de cadenas. Con una sola línea puedo asegurar que la estructura de la hora sea la correcta. Si lo hubiera hecho con condicionales, habría necesitado muchos if y comprobaciones, lo que complicaría el mantenimiento del código.

7. ¿Por qué es mejor usar expresiones regulares que muchos if?

La respuesta realmento no varía en exceso en relación con la pregunta 6: las expresiones regulares me permiten validar toda la estructura de la hora con una sola instrucción clara y concisa. Esto hace que el código sea más limpio, legible y fácil de mantener. Si hubiera usado varios if, habría terminado con una validación más extensa, repetitiva y difícil de modificar en el futuro. 



































