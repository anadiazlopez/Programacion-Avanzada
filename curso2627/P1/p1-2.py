
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def leap_years_between(start, end):
    lista_bisiestos = []
    for year in range (start, end + 1, 1):
        if is_leap_year(year):
            lista_bisiestos.append(year)
    return lista_bisiestos


def explain_leap_year(year):
    if is_leap_year(year):
        if year % 4 == 0 and year % 100 != 0:
            return f"{year} es bisiesto: es divisible entre 4 y no entre 100."
        else:
            return f"{year} es bisiesto: es divisible entre 400."
    else:
        if year % 100 == 0:
            return f"{year} no es bisiesto: es divisible entre 100 pero no entre 400."
        else:
            return f"{year} no es bisiesto: no es divisible entre 4."

def main():
    año = int(input("Introduce un año: "))
    if año < 1582:
        print("El calendario gregoriano se estableció en 1582.")
    else:
        resultado = explain_leap_year(año)
        print(resultado)

    print("=*" * 60)
    
    # leap_years_between 
    inicio = 1896
    fin = 1912
    lista_bisiestos = leap_years_between(inicio, fin)
    print(f">>> leap_years_between({inicio}, {fin})\n{lista_bisiestos}")

if __name__ == "__main__":
    main()

