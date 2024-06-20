
def calcula_grau(vertice, lista_adj_grafo):
    grau = 0
    for ligacoes in lista_adj_grafo:
        for v in ligacoes:
            if v == vertice:
                grau += 1
    
    for v in lista_adj_grafo[vertice]:
        grau += 1
    
    return grau