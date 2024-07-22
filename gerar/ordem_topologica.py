from cores import Cores
def dfs(lista_adj, idx, cores, ordem = []):
    cores[idx] = Cores.CINZA

    for e in enumerate(lista_adj[idx]):
        if cores[e] == Cores.BRANCO:
            dfs(lista_adj, e, cores)

    cores[idx] = Cores.PRETO
    ordem.insert(0, idx)


def gera_ordem_topologica(lista_adj):
    tam = 0
    for _ in lista_adj:
        tam += 1
    
    cores = [Cores.BRANCO for _ in range(tam)]
    ordem = []

    for idx, c in enumerate(cores):
        if c == Cores.BRANCO:
            dfs(lista_adj, idx, cores, ordem)
    
    return ordem