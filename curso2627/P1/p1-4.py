def shift_char(char, shift):
    if char.islower():
        nueva_pos = (ord(char) - ord('a') + shift) % 26
        return chr(ord('a') + nueva_pos)
    
    elif char.isupper():
        nueva_pos = (ord(char) - ord('A') + shift) % 26
        return chr(ord('A') + nueva_pos)
        
    else:
        return char

def encrypt(text, shift):
    lista = []
    for c in text:
        lista.append(shift_char(c, shift))
    return "".join(lista)

def decrypt(text, shift):
    lista = []
    for c in text:
        lista.append(shift_char(c, -shift))
    return "".join(lista)

def brute_force(cipher_text):
    lista = []
    print("\n","=*" * 40,"\nPosibles soluciones:\n")
    for i in range(26):
        lista.append(decrypt(cipher_text, i))
    return lista

def main():
    cadena1 = "Hola, Mundo!"
    cadena2 = "xyz"

    cadena1 = encrypt(cadena1, 3)
    print(cadena1)

    cadena1_1 = decrypt(cadena1, 3)
    print(cadena1_1)

    cadena2 = encrypt(cadena2, 3)
    print(cadena2)

    cadena2 = encrypt(cadena2, -3)
    print(cadena2) 

    cadena1 = brute_force(cadena1)
    print(cadena1)

if __name__ == "__main__":
    main()