def is_pangram(sentence):
    letras = []
    for letra in sentence:
        if letra.isalpha():
            letras.append(letra.lower())
    pangram = True
    for num in range(97, 123):
        caracter = chr(num)
        if caracter not in letras:
            pangram = False
            return pangram
    return pangram
