from cores import Cores

def gerar_arvore_bfs(lista_adj):

    cores = [Cores.BRANCO for _ in range(len(lista_adj))]

    fila = [0]
    for i in fila:
        cores[i] = Cores.CINZA

        for j in lista_adj[i]:
            if cores[j] == Cores.BRANCO and not (j in fila):
                fila.append(j)
        cores[i] = Cores.PRETO
    
    return fila