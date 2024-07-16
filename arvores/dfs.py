from .cores import Cores

def dfs(matriz_adj, idx, cores, arvore):
    cores[idx] = Cores.CINZA
    arvore.append(idx)

    for idx_, l in enumerate(matriz_adj[idx]):
        if l == 1 and cores[idx_] == Cores.BRANCO:
            dfs(matriz_adj, idx_, cores, arvore)
    
    cores[idx] = Cores.PRETO