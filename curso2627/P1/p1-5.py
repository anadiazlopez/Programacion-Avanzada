def normalize(text):
    lista = []
    for c in text:
        new_c = c.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ü', 'u')
        lista.append(new_c)
    return "".join(lista)
    
def is_palindrome(text):
    texto_limpio = normalize(text)
    texto_final = ""
    for c in texto_limpio:
        if c.isalnum():  
            texto_final += c

    return texto_final == texto_final[::-1]

def find_palindrome(sentences):
    lista = []
    for i in range(len(sentences)):
        if is_palindrome(sentences[i]):
            lista.append(sentences[i])
    return lista

def palindrome_words(text):
    lista = text.split()
    lista_palabras = find_palindrome(lista)
    print(lista_palabras)

def main():
    sentences = [
        "Anita lava la tina",
        "Dábale arroz a la zorra el abad",
        "Esto no es un palíndromo",
        "¿Acaso hubo búhos acá?",
    ]

    lista_frases = find_palindrome(sentences)
    print(lista_frases)
    palindrome_words("Ana vio un oso en el ojo de Anita")

if __name__ == "__main__":
    main()