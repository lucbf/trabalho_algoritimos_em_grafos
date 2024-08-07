class MatrizAdj:

    '''
    Dados vértices e arestas cria uma matriz de 
    adjacência
    '''
    def __init__(self, vertices, arestas) -> None:
        self.matriz_adj = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]

        for a, b, _ in arestas:
            self.matriz_adj[a][b] = 1
    
    def __str__(self) -> str:
        retorno = ''
        for lista in self.matriz_adj:
            retorno += lista.__str__() + '\n'
        
        return retorno
    
class MatrizAdjValorada:

    def __init__(self, vertices, arestas):
        self.matriz_adj = [[None for _ in range(len(vertices))] for _ in range(len(vertices))]

        for a, b, p in arestas:
            self.matriz_adj[a][b] = p