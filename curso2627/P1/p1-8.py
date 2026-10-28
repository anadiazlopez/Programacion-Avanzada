
def suma_total(lista):
    resultado = 0
    for i in lista:
        resultado += i
    return resultado

def pos_neg(lista):
    pos = []
    neg = []
    for i in lista:
        if i >= 0:
            pos.append(i)
        else:
            neg.append(i)

    return pos, neg

def max_min(lista):
    lista.sort() 
    print('Número mínimo:', lista[0])
    print('Número máximo:', lista[len(lista) - 1])

def unicos(lista):
    return len(lista) == len(set(lista)) # set() no permite duplicados

def cantidad_pos_neg(lista):
    pos, neg = pos_neg(lista)
    return 'positivos' if len(pos) > len(neg) else 'negativos'

def menu(lista):

    print("1. Suma de todos los números.")
    print("2. Suma de los números positivos y suma de los números negativos .")
    print("3. Encuentra el número máximo y el mínimo.")
    print("4. Comprueba si todos los números de la lista son únicos.")
    print("5. ¿Hay más positivos o negativos?")

    opcion = int(input("\nSelecciona una opción (1 - 5): "))

    if opcion == 1:
        print(suma_total(lista))
    elif opcion == 2:
        pos, neg = pos_neg(lista)
        print("\nLista de positivos:", pos, ' --> Suma:', suma_total(pos))
        print("Lista de negativos:", neg,' --> Suma:', suma_total(neg))
    elif opcion == 3:
        max_min(lista)
    elif opcion == 4:
        if unicos(lista) ==  False:
            print('Hay números que se repiten.')
        else:
            print('Todos los números de la lista son únicos.')
    elif opcion == 5:
        print('En la lista hay más números', cantidad_pos_neg(lista),'.')
    elif opcion == 6:
        print('Saliendo...')
        return 6
    else:
        return False

def main():
    lista = [-15, 2, -3, 8, 19, 0, -9, -11, 14, 2, 5] 
    print('LISTA INICIAL:', lista)
    while True:
        resultado = menu(lista)
        if resultado == 6:
            break
        elif resultado is False:
            print("El dato introducido es erróneo. Vuelve a intentarlo.")

if __name__ == "__main__":
    main()
















































