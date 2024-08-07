from .cores import Cores




def dfs_entrada_saida(matriz_adj, vertice, tempo_entrada_saida, tempo):
    tempo += 1
    tempo_entrada_saida[vertice][0] = tempo

    for idx, e in enumerate(matriz_adj[vertice]):
        if e == 1 and tempo_entrada_saida[idx][0] == 0:
            tempo = dfs_entrada_saida(matriz_adj, idx, tempo_entrada_saida, tempo)
    
    tempo += 1
    tempo_entrada_saida[vertice][1] = tempo

    return tempo

def dfs_inverso(matriz_adj, vertice, cores, vertices_percorridos):
    cores[vertice] = Cores.CINZA
    vertices_percorridos.append(vertice)

    for idx, l in enumerate(matriz_adj):
        if l[vertice] == 1 and cores[idx] == Cores.BRANCO:
            dfs_inverso(matriz_adj, idx, cores, vertices_percorridos)
    
    cores[vertice] = Cores.PRETO


def gerar_lista_conexidade_forte(matriz_adj):
    tam = 0
    for _ in matriz_adj:
        tam += 1
    i = 0
    tempo_entrada_saida = []
    while i < tam:
        tempo_entrada_saida.append([0,0])
        i += 1

    i = 0
    tempo = 0
    while i < tam:
        if tempo_entrada_saida[i][0] == 0:
            tempo = dfs_entrada_saida(matriz_adj, i, tempo_entrada_saida, tempo)
        i += 1

    
    cores = [Cores.BRANCO for _ in range(tam)]
    lista_conexidade_forte = []
    i = 0
    while i < tam:
        if cores[i] == Cores.BRANCO:
            elemento_lista = []
            dfs_inverso(matriz_adj, i, cores, elemento_lista)
            lista_conexidade_forte.append(elemento_lista)
        i += 1
    return lista_conexidade_forte
