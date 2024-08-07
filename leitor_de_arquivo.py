import os.path
from erro import imprimir_erro

class LeitorDeArquivo:
    def __init__(self, arquivo):
        if os.path.isfile(arquivo):
            self.arquivo = arquivo
        else:
            imprimir_erro(arquivo + " não é um arquivo.")

    '''
    Lê arquivo e retorna os vértices, as arestas e se o grafo é
    direcionado ou não
    '''
    def interpretar(self):
        aq_ = open(self.arquivo)
        aq = aq_.read()
        aq_.close()

        aq = aq.split('\n')

        vertices = []
        arestas = []

        linha1 = aq[0].split(' ')
        nvertices = int(linha1[0])
        narestas = int(linha1[1])

        direcionado = False
        if aq[1] == 'direcionado':
            direcionado = True

        i = 2
        tam = i + narestas
        while i < tam:
            linha = aq[i].split(' ')
            aresta = (int(linha[1]), int(linha[2]), int(linha[3]))
            arestas.append(aresta)

            if not direcionado:
                aresta2 = (aresta[1], aresta[0], aresta[2])
                arestas.append(aresta2)

            i += 1
        
        for n in range(nvertices):
            vertices.append(n)
        return (vertices, arestas, direcionado)

