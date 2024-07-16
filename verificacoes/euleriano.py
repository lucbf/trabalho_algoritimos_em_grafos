from .grau import calcula_grau


def verifica_euleriano(lista_adj):
    tam = 0
    for _ in lista_adj:
        tam += 1
    

    graus_impares = 0
    graus_pares = 0
    v = 0
    while v < tam:
        if calcula_grau(v, lista_adj) % 2:
            graus_impares += 1
        else:
            graus_pares += 1
        v += 1
    
    if graus_impares == 2:
        return "Semi-Euleriano"
    elif graus_impares == 0:
        return "Euleriano"
    else:
        return "Não é Euleriano"

