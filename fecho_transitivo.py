from sys import maxsize

def calcula_fecho_transitivo(matriz_adj):
    #prepara matriz de adjacência
    ma = []
    for lista in matriz_adj:
        ma.append([])
        for i, e in enumerate(lista):
            if e == 0:
                ma[-1].append(maxsize)
            else:
                ma[-1].append(i)
    for i in range(len(ma)):
        ma[i][i] = i

    #floyd-warshall
    for k in range(len(ma)):
        for i in range(len(ma)):
            for j in range(len(ma)):
                if ma[i][k] + ma[k][j] < ma[i][j]:
                    ma[i][j] = j
    
    for e in ma[0]:
        if e >= maxsize:
            del e
    
    return ma[0]
