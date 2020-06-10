def convert(numero):

    i = 1
    divisibles = []
    while i <= numero:
        if numero % i == 0:
            divisibles .append(i)
        i += 1
    print(divisibles)

    resultado = ''
    if 3 in divisibles:
        resultado += 'Pling'
    if 5 in divisibles:
        resultado += 'Plang'
    if 7 in divisibles:
        resultado += 'Plong'
    if not resultado:
        resultado += str(numero)

    return resultado
