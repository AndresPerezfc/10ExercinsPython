import math


def score(x, y):

    distancia = math.sqrt((x*x)+(y*y))
    if distancia > 1 and distancia <= 5:
        return 5
    elif distancia > 5 and distancia <= 10:
        return 1
    elif distancia <= 1:
        return 10
    else:
        return 0
