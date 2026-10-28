def is_prime(n):
    contador = 0
    for i in range (2, n):
        if n % i == 0:
            contador += 1
    return contador == 0 and n > 1

def prime_list(limit):
    lista_primos = []
    for i in range(2, limit + 1):
        if is_prime(i):
            lista_primos.append(i)
    return lista_primos

def check_palindrome(primes):
    lista_palin = []
    for i in primes:
        i = str(i)
        if i == i[::-1]:
            lista_palin.append(i)
    return lista_palin

def categorize_prime(prime):
    if prime < 10:
        return "p"
    if prime >= 10 and prime < 100:
        return "m"
    if prime >= 100:
        return "g"
    
def main():
    lista_numeros = [53, 1, 6, 34, 34, 11, 55, 17, 9, 67, 31, 22]
    lista_resultados = []

    for i in range(len(lista_numeros)):
        lista_resultados.append(is_prime(lista_numeros[i]))
    print(lista_resultados)

    lista_resultados = prime_list(150)
    print(lista_resultados)

    print(check_palindrome(lista_resultados))

    peq = []
    med = []
    grand = []
    for i in range(len(lista_resultados)):
        tam = categorize_prime(lista_resultados[i])
        if tam == "p":
            peq.append(lista_resultados[i])
        elif tam == "m":
            med.append(lista_resultados[i])
        if tam == "g":
            grand.append(lista_resultados[i])

    print(f"\nNúmeros pequeños: {peq}\nNúmeros medianos: {med}\nNúmeros grandes: {grand}")
            
if __name__ == "__main__":
    main()
















































