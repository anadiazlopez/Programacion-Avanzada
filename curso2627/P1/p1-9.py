def format_monomial(coef, exp):
    n = str(coef)
    if coef > 1:
        if exp == 0:
            n = f'+{coef}'
        elif exp == 1:
            n = f'+{coef}x'
        else:
            n = f'+{coef}x**{exp}'

    elif coef == 1:
        if exp == 0:
            n = '+1'
        elif exp == 1:
            n = f'+x'
        else:
            n = f'+x**{exp}'

    elif coef == 0:
        n = ''

    else:
        if exp == 0:
            n = f'{coef}'
        elif exp == 1:
            n = f'{coef}x'
        else:
            n = f'{coef}x**{exp}'

    return n
    
def format_polynomial(coefs):
    polinomio = ''

    for i in range(len(coefs) - 1, -1, -1):
        coef = coefs[i]                 
        exp = i    
        monomio = format_monomial(coef, exp)
        polinomio += monomio

    if polinomio and polinomio[0] == '+':
        polinomio = polinomio[1:]

    polinomio = polinomio.replace('+', ' + ').replace('-', ' - ')

    # Tras añadir los espacios, si el primer coeficiente es - algo al principio del polinomio aparecerá un espacio innecesario.
    # Entonces, si el primer caracter es un espacio en blanco, se suprime:
    if polinomio and polinomio[0] == ' ': 
        polinomio = polinomio[1:]

    return polinomio

def evaluate(coefs, x):
    if not coefs:
        return 0

    valor = 0
    for i, coef in enumerate(coefs):
        valor += coef * (x ** i)

    return valor
        
def derivate(coefs):
    if len(coefs) <= 1:
        return []
    derivada = []
    # coefs[1:] para ignorar la constante e 'i' empieza en 1
    for i, coef in enumerate(coefs[1:], 1):
        coef = coef * i
        derivada.append(coef)
    return derivada

def main():
    lista1 = [4.0, 1.0, 0.0, 2.0]
    lista2 = [-2.0, 5.5, 1.0, 0.0, -5.0]
    coefs = lista2
    exp = len(coefs) - 1
    x = 2
   
    for i in range(len(coefs) - 1, -1, -1):
        coef = coefs[i]
        n = format_monomial(coef, exp)
        print(n)
        exp -= 1
    
    print(format_polynomial(coefs))

    print(evaluate(coefs, x))

    print(derivate(coefs))

if __name__ == "__main__":
    main()












































