from cores import Cores

def encontra_ciclo(lista_adj, idx, idx_inicial, arestas_visitadas, caminho, direcionado):
    caminho.append(idx)

    for e in lista_adj[idx]:
        if not ((idx, e) in arestas_visitadas) or (not direcionado and not ((e, idx) in arestas_visitadas)):
            arestas_visitadas.add((idx, e))
            if not direcionado:
                arestas_visitadas.add((e, idx))
            if e == idx_inicial or encontra_ciclo(lista_adj, e, idx_inicial, arestas_visitadas, caminho, direcionado):
                return True
            
    return False

def calcula_grau_balanceado(lista_adj, v):
    grau = 0
    for a in lista_adj:
        for b in a:
            if b == v:
                grau += 1
    for _ in lista_adj[v]:
        grau -= 1

def calcula_grau(lista_adj, v):
    grau = 0
    for _ in lista_adj[v]:
        grau += 1
    
    return grau

def verifica_pseudosimetrico(lista_adj, direcionado):
    if direcionado:
        for idx in range(len(lista_adj)):
            if calcula_grau_balanceado(lista_adj, idx) != 0:
                return False
    else:
        for idx in range(len(lista_adj)):
            if calcula_grau(lista_adj, idx) % 2 == 1:
                return False
    return True

def gerar_caminho_euleriano(lista_adj, direcionado):
    i = 0
    if not verifica_pseudosimetrico(lista_adj, direcionado):
        return []
    
    arestas_visitadas = []
    caminho = set()
    while i < len(lista_adj):
        c = []
        if not encontra_ciclo(lista_adj, i, i, arestas_visitadas, c, direcionado):
            i += 1
        else:
            if caminho != []:
                for idx, cam in caminho:
                    if cam == i:
                        del caminho[idx]
                        c.reverse()
                        for e in c:
                            caminho.insert(idx, e)
            else:
                caminho = c
    
    return caminho
