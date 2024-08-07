class ListaAdj:
    '''
    Dados vértices e arestas, cria uma lista
    de adjacência
    '''
    def __init__(self, vertices, arestas):        
        self.lista_adj = [[] for _ in range(len(vertices))]

        for v1, v2, _ in arestas:
            self.lista_adj[v1].append(v2)
    
    def __str__(self) -> str:
        return self.lista_adj.__str__()
    
class ListaAdjValorada:

    def __init__(self, vertices, arestas):
        self.lista_adj = [[] for _ in range(len(vertices))]

        for v1, v2, p in arestas:
            self.lista_adj[v1].append((v2, p))