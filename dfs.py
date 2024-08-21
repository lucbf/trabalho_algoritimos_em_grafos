from cores import Cores

def dfs(lista_adj, idx, cores, arvore):
    cores[idx] = Cores.CINZA
    arvore.append(idx)

    for e in lista_adj[idx]:
        if cores[e] == Cores.BRANCO:
            dfs(lista_adj, e, cores, arvore)
    
    cores[idx] = Cores.PRETO

def gerar_arvore_dfs(lista_adj):
    arvore = []

    tam = 0
    for _ in lista_adj:
        tam += 1

    cores = [Cores.BRANCO for _ in range(tam)]

    dfs(lista_adj, 0, cores, arvore)
    
    return arvore