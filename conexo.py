from cores import Cores

def dfs(lista_adj, idx, cores):
    cores[idx] = Cores.CINZA

    for e in enumerate(lista_adj[idx]):
        if cores[e] == Cores.BRANCO:
            dfs(lista_adj, e, cores)

    cores[idx] = Cores.PRETO


def verifica_conexo(lista_adj):
    tam = 0
    for _ in lista_adj:
        tam += 1

    cores = [Cores.BRANCO for _ in range(tam)]

    dfs(lista_adj, 0, cores)

    for c in cores:
        if c != Cores.PRETO:
            return False
    else:
        return True