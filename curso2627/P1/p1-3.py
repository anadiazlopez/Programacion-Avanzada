def process_text(cadena, lista):
    cadena_lista = cadena.split(" ")
    contador = 0
    nueva_lista = []
    for i in cadena_lista:
        if i in lista:
            nueva_lista.append("*" * len(i))
            contador = contador + 1
        else:
            nueva_lista.append(i.lower())

    nueva_cadena = " ".join(nueva_lista)

    return nueva_cadena, contador
      

def main():
    cadena = "This is a default text with Python and amazing words."
    lista = ["Python", "amazing"]

    nueva_cadena, contador = process_text(cadena, lista)
    print(nueva_cadena)
    print("Palabras reemplazadas:", contador)


if __name__ == "__main__":
    main()
