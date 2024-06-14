class MatrizAdj:

    '''
    Dados vértices e arestas cria uma matriz de 
    adjacência
    '''
    def __init__(self, vertices, arestas, direcionado) -> None:
        nvertices = 0
        for v in vertices:
            if v + 1 > nvertices:
                nvertices = v + 1

        self.matriz_adj = [[0 for _ in range(nvertices)] for _ in range(nvertices)]

        for a, b in arestas:
            self.matriz_adj[a][b] = 1
            if not direcionado:
                self.matriz_adj[b][a] = 1
    
    def __str__(self) -> str:
        retorno = ''
        for lista in self.matriz_adj:
            retorno += lista.__str__() + '\n'
        
        return retorno