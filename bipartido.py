from cores import Cores

def dfs_bipartido(lista_adj, cores, idx, cor_atual = Cores.CINZA, bipartido = True):
    cores[idx] = cor_atual

    for v in lista_adj[idx]:
        if cores[v] == cor_atual:
            bipartido = False
            break
        elif cores[v] == Cores.BRANCO:
            cor = Cores.BRANCO
            if cor_atual == Cores.CINZA:
                cor = Cores.PRETO
            else:
                cor = Cores.PRETO
            bipartido = dfs_bipartido(lista_adj, cores, v, cor, bipartido)
            if bipartido == False:
                break
    
    return bipartido

def verifica_bipartido(lista_adj):

    tam = 0
    for i in lista_adj:
        tam += 1

    cores = [Cores.BRANCO for _ in range(tam)]
    
    bipartido = True
    for idx, c in enumerate(cores):
        if c == Cores.BRANCO:
            bipartido = dfs_bipartido(lista_adj, cores, idx)
            if not bipartido:
                break
    
    return bipartido