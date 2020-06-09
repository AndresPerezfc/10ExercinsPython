def is_isogram(string):
    alfabeto = "qwertyuiopñlkjhgfdsazxcvbnm"
    
    for letra in alfabeto:
        print("Letra: " +letra)
        contador = 0
        for letraEnPalabra in string:
            print("Letra de la palabra: " +letraEnPalabra)
            if letra == letraEnPalabra.lower():
               # print("Palabra: " + palabra.lower())
                contador = contador + 1
            
            if contador > 1:
                return False
            
    return True
        
is_isogram("hola")