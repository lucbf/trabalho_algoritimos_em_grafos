from cores import Cores

def dfs_ciclo(lista_adj, idx, cores, achou_ciclo = False):
    cores[idx] = Cores.CINZA

    for v in lista_adj[idx]:
        if cores[v] == Cores.BRANCO:
            achou_ciclo = dfs_ciclo(lista_adj, v, cores, achou_ciclo)
            if achou_ciclo:
                break
        else:
            achou_ciclo = True
            break
    
    cores[idx] = Cores.PRETO
    return achou_ciclo

def verificar_ciclos(lista_adj):
    ciclos = False
    
    cores = [Cores.BRANCO for _ in range(len(lista_adj))]

    for idx, c in enumerate(cores):
        if c == Cores.BRANCO:
            ciclos = dfs_ciclo(lista_adj, idx, cores)
            if ciclos:
                break
    return ciclos

