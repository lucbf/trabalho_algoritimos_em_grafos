from cores import Cores

class Ordem:
    def __init__(self) -> None:
        self.entrada = -1
        self.saida = -1

def dfs_ida(matriz_adj, idx, e_s, tempo):
    e_s[idx].entrada = tempo

    for i in matriz_adj[idx]:
        if i == 1 and e_s[i].entrada == -1:
            tempo = dfs_ida(matriz_adj, i, e_s, tempo + 1)
    
    tempo += 1
    e_s[idx].saida = tempo

    return tempo

def dfs_volta(matriz_adj, idx, cores, lista):
    cores[idx] = Cores.CINZA
    lista.append(idx)

    i = 0
    while i < len(matriz_adj):
        if matriz_adj[i][idx] == 1 and cores[i] == Cores.BRANCO:
            dfs_volta(matriz_adj, i, cores, lista)
        i += 1
    cores[idx] = Cores.PRETO

def lista_comp_fortemente_conexas(matriz_adj):
    e_s = [Ordem() for _ in range(len(matriz_adj))]
    cores = [Cores.BRANCO for _ in range(len(matriz_adj))]
    tempo = 1
    for idx, c in enumerate(cores):
        if c == Cores.BRANCO:
            tempo = dfs_ida(matriz_adj, idx, e_s, tempo)

    cores = [Cores.BRANCO for _ in range(len(matriz_adj))]
    componentes = []
    while Cores.BRANCO in cores:
        maior = (0, 0)
        for idx, v in enumerate(e_s):
            if cores[idx] == Cores.BRANCO and v.saida > maior[1]:
                maior = (idx, v.saida)
        componente = []
        dfs_volta(matriz_adj, maior[0], cores, componente)
        componentes.append(componente)
    
    return componentes