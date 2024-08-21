import sys
def dfs_ponte(lista_adj, idx, idx_anterior, tempo, tempos, indicadores, arestas_ponte):
    tempo += 1
    tempos[idx] = tempo
    indicadores[idx] = tempo

    for v in lista_adj[idx]:
        if tempos[v] == sys.maxsize:
            indicadores[idx] = min(dfs_ponte(lista_adj, v, idx, tempo, tempos, indicadores, arestas_ponte), indicadores[idx])
            if indicadores[v] > indicadores[idx]:
                arestas_ponte[0] += 1
        elif v != idx_anterior:
            indicadores[idx] = indicadores[v]
    
    return indicadores[idx]


def qtd_arestas_ponte(lista_adj, direcionado):
    if direcionado:
        return "-1"
    tempos = [sys.maxsize for _ in range(len(lista_adj))]
    indicadores = tempos.copy()
    arestas_ponte = [0]

    for idx, t in enumerate(tempos):
        if t == sys.maxsize:
            dfs_ponte(lista_adj, idx, -1, 0, tempos, indicadores, arestas_ponte)
    
    return arestas_ponte[0]
    
