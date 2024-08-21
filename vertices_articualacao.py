from cores import Cores
from queue import Queue

#se o grau for menor que 2 não é um vértice de articulação
def analisa_candidato(lista_adj, vertice):
    grau = 0
    for _ in lista_adj[vertice]:
        grau += 1
        if grau == 2:
            return True
    return False

def vertices_articulacao(lista_adj, direcionado):
    if direcionado:
        return [-1]
    
    retorno = []

    for vertice_analisado in range(len(lista_adj)):
        if analisa_candidato(lista_adj, vertice_analisado):
            cores = [Cores.BRANCO for _ in range(len(lista_adj))]
            cores[vertice_analisado] = Cores.PRETO #necessário para que a busca não passe pelo vértice
            #bfs
            fila = Queue(len(lista_adj) - 2)#excluindo vértice atual e o vértice analisado
            fila.put(lista_adj[vertice_analisado][0])
            while not fila.empty():
                v1 = fila.get()
                cores[v1] = Cores.CINZA
                for v2 in lista_adj[v1]:
                    if cores[v2] == Cores.BRANCO:
                        fila.put(v2)
                cores[v1] = Cores.PRETO
            if Cores.BRANCO in cores:
                retorno.append(vertice_analisado)
        
    if retorno == []:
        retorno.append(-1)
    return retorno
