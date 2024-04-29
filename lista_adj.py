class ListaAdj:
    '''
    Dados vértices e arestas, cria uma lista
    de adjacência
    '''
    def __init__(self, vertices, arestas):
        nvertices = 0
        for v in vertices:
            if v + 1 > nvertices:
                nvertices = v + 1
        
        self.lista_adj = [[] for _ in range(nvertices)]

        for v1, v2 in arestas:
            self.lista_adj[v1].append(v2)