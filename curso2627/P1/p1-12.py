def is_anagram(word1, word2):
    # sorted(x): devuelve una nueva lista con sus elementos ordenados
    return sorted(word1.lower().replace(" ", "")) == sorted(word2.lower().replace(" ", ""))

def group_anagrams(words):
    lista_de_listas = []
    
    for word in words:
        encontrado = False
        for grupo in lista_de_listas:
            if is_anagram(word, grupo[0]):
                grupo.append(word)
                encontrado = True
                break
        
        if not encontrado:
            lista_de_listas.append([word])
            
    return lista_de_listas

def largest_group(groups):
    return [] if not groups else max(groups, key=len)

def find_anagrams(word, words):
    anagrams = []
    for w in words:
        if is_anagram(word, w) and w != word:
            anagrams.append(w)
    return anagrams

def main():
    words = ["roma", "amor", "pelo", "mora", "casa", "lope", "ramo"]

    print( 
        is_anagram("Roma", "amor"),"\n",
        is_anagram("casa", "caso"),"\n",
        is_anagram("dormitory", "dirty room"),"\n\n",
        
        group_anagrams(words),"\n","\n",
        
        largest_group(group_anagrams(words)),"\n\n",

        find_anagrams("amor", words),"\n",
        find_anagrams("amor", ["amor", "roma", "AMOR", "roma"]),"\n",
        find_anagrams("sol", words) )


if __name__ == "__main__":
    main()