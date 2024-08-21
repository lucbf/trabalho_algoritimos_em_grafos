from cores import Cores
from queue import Queue

def comp_conexos(lista_adj):
    cores = [Cores.BRANCO for _ in range(len(lista_adj))]
    retorno = 0

    for idx, c in enumerate(cores):
        if c == Cores.BRANCO:
            #considerando um grafo completo, o número de
            #vértices que conectam com outro é n -1, portanto
            #a fila tem o tamanho máximo de n - 1 pois o primeiro
            #vértice é retirado dela na primeira iteração
            fila = Queue(len(lista_adj) - 1)
            fila.put(idx)
            retorno += 1
            #bfs
            while not fila.empty():
                v = fila.get()
                cores[v] = Cores.CINZA

                for adj in lista_adj[v]:
                    if cores[adj] == Cores.BRANCO:
                        fila.put(adj)
                cores[v] = Cores.PRETO
    return retorno

