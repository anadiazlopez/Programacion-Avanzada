def remove_duplicates(numbers):
    lista_final = []
    for i in numbers:
        if i not in lista_final:
            lista_final.append(i)
    return lista_final

def rotate_left(numbers, k):
    k = k % len(numbers)
    return numbers[k:] + numbers[:k]

def split_even_odd(numbers): # Lista pares e impares
    pares, impares = [], []
    for i in numbers:
        if i % 2 == 0:
            pares.append(i)
        else: 
            impares.append(i)
    return [pares, impares]

def merge_sorted(a, b): # Recibe dos listas ya ordenadas de menor a mayor y
                        # devuelve una única lista ordenada. Recorra ambas listas a la vez con dos índices,
                        # sin ordenar el resultado final
    lista_ord = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            lista_ord.append(a[i])
            i += 1
        else:
            lista_ord.append(b[j])
            j += 1

    lista_ord.extend(a[i:]) # Los elementos que faltan por añadir
    lista_ord.extend(b[j:])

    return lista_ord

def second_largest(numbers): 
    
    if not numbers or len(numbers) < 2 or len(remove_duplicates(numbers)) == 1:
        return None

    numbers = remove_duplicates(numbers)
    numbers.sort() # Ordena de MENOR a MAYOR

    return numbers[-2]
    
def main():
    lista = [1, 2, 3, 4, 5, 6]

    print(remove_duplicates([3, 1, 3, 2, 1,]))
    print('*=' * 30)
    
    print(rotate_left(lista, 2))
    print(rotate_left(lista, -3))
    print(rotate_left(lista, 0))
    print('*=' * 30)

    print(split_even_odd(lista))
    print('*=' * 30)

    print(merge_sorted([3, 6, 9], [2, 4, 8]))
    print('*=' * 30)

    print(second_largest([4, 5, 22, 7, 10, 34, 4, 0, -1, 3]))
    print(second_largest([5, 5]))
    print('*=' * 30)


if __name__ == "__main__":
    main()





