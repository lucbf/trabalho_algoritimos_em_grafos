from .cores import Cores

def bfs(lista_adj):
    tam = 0
    for _ in lista_adj:
        tam += 1

    cores = [Cores.BRANCO for _ in range(tam)]

    fila = [0]
    for i in fila:
        cores[i] = Cores.CINZA

        for j in lista_adj[i]:
            if cores[j] == Cores.BRANCO and not (j in fila):
                fila.append(j)
        cores[i] = Cores.PRETO
    
    return fila