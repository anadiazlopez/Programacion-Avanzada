def imprimir_cadena(lista_cad, letra):
    for cadena in lista_cad:
        if cadena[0].lower() == letra.lower():
            print(cadena)
def contar_subcadena(lista_cad):
    subcadena = input("Introduce la subcadena que deseas buscar: ")
    contador = 0
    
    for cadena in lista_cad:
        if subcadena.lower() in cadena.lower():  
            contador += 1
            
    print(f"La subcadena '{subcadena}' aparece en {contador} cadena(s).")

def longitud_cadena(lista_cad):
    print('Cadena más larga:', max(lista_cad, key=len))
    print('Cadena más corta:', min(lista_cad, key=len))

def comparar_cadenas(lista_cad):
    encontrado = False
    for i in range(len(lista_cad)):
        for j in range(i + 1, len(lista_cad)):
            if lista_cad[i] is lista_cad[j]:
                print(f"Coincidencia de obejto: '{lista_cad[i]}'")
                encontrado = True
                
    if not encontrado:
        print("No hay ninguna cadena en la lista que comparta el mismo objeto en memoria.")

def mayor_que_10(lista_cad):
    encontrado = False
    for cadena in lista_cad:
        if len(cadena) > 10:
            print(f"'{cadena}' --> {len(cadena)} caracteres.")
            encontrado = True
            
    if not encontrado:
        print("Ninguna cadena tiene más de 10 caracteres.")

def menu(lista_cad):

    print("1. Imprima cada cadena que comience con una letra pedida al usuario.")
    print("2. Cuente cuántas cadenas contienen una subcadena pedida al usuario.")
    print("3. Encuentre la cadena más larga y la más corta de la lista.")
    print("4. Verificar si dos cadenas específicas de la lista son en realidad el mismo objeto.")
    print("5. Verificar si alguna cadena de la lista tiene una longitud mayor que 10.")
    print("6. Salir.")

    
    print(lista_cad)
    opcion = int(input("\nSelecciona una opción (1 - 6): "))

    if opcion == 1:
        letra = input("Introduce letra: ")
        if len(letra) != 1:
            print('Solo se puede introducir una letra.')
        else:
            imprimir_cadena(lista_cad, letra)
    elif opcion == 2:
        contar_subcadena(lista_cad)
    elif opcion == 3:
        longitud_cadena(lista_cad)
    elif opcion == 4:
        comparar_cadenas(lista_cad)
    elif opcion == 5:
       mayor_que_10(lista_cad)
    elif opcion == 6:
        print("Saliendo...")
        return 6
    else:
        return False
        
def main():
    palabra = 'hola'
    lista_cad = [palabra, 'que tal', palabra]

    while True:
        cad = input("Escribe una frase (introduce 'Enter' para parar): ")
        if cad == "":
            break
        lista_cad.append(cad)

    if not lista_cad:
        print("No se ha introducido ninguna cadena.")
        return
    
    while True:
        resultado = menu(lista_cad)
        if resultado == 6:
            break
        elif resultado is False:
            print("El dato introducido es erróneo. Vuelve a intentarlo.")
      

if __name__ == "__main__":
    main()
