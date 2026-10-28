
def is_integer(text):
    try:
        dato = int(text)
        if dato > 0:
            return True
        else:
            print("Entrada no válida. Introduzca un entero no negativo.")
            return False
    except:
        print("Entrada no válida. Introduzca un entero no negativo.")
        return False

def seconds_to_dhms(total_seconds):
    # 1 día = 86.400 segundos -> 24 horas x 60 minutos x 60 segundos 
    # 1 hora = 3600 segundos  
    # 1 min = 60 segundos 

    dias = total_seconds // 86400
    resto = total_seconds % 86400

    horas = resto // 3600
    resto = resto % 3600

    minutos = resto // 60
    segundos = resto % 60

    return (dias, horas, minutos, segundos)



def main():
    text = input("Introduzca los segundos: ")

    if is_integer(text):
        print("El valor introduciod es correcto.")
        d, h, m, s = seconds_to_dhms(int(text))
        print(f"{text} segundos son {d} d, {h} h, {m} min y {s} s.")

    else:
        main()

if __name__ == "__main__":
    main()







