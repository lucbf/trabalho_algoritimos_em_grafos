class ListaAdj:
    '''
    Dados vértices e arestas, cria uma lista
    de adjacência
    '''
    def __init__(self, vertices, arestas, direcionado):
        nvertices = 0
        for v in vertices:
            if v + 1 > nvertices:
                nvertices = v + 1
        
        self.lista_adj = [[] for _ in range(nvertices)]

        for v1, v2 in arestas:
            self.lista_adj[v1].append(v2)
            if not direcionado:
                self.lista_adj[v2].append(v1)
    
    def __str__(self) -> str:
        return self.lista_adj.__str__()