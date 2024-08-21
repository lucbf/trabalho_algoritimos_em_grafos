from sys import maxsize

def constroi_caminho(i, pais, explorados, caminho):
    caminho.insert(0, i)
    explorados.add(i)

    if i != 0 and not pais[i] in explorados:
        constroi_caminho(pais[i], pais, explorados, caminho)


def dijkstra(lista_adj_valorada, matriz_adj_valorada):
    inicio = 0
    fim = len(lista_adj_valorada) - 1

    #(Vértice, valor relaxação, explorado)
    vertices = [[v, maxsize, False] for v in range(len(lista_adj_valorada))]
    pais = [0 for v in range(len(lista_adj_valorada))]
    vertices[0] = [0, 0, True]

    i = 0
    while i >= 0:
        for v in lista_adj_valorada[i]:
            if not vertices[v[0]][2] and v[1] < vertices[v[0]][1]:
                vertices[v[0]] = [v[0], v[1], False]
                pais[v[0]] = i
        vertices[i][2] = True

        menor = (-1, maxsize)
        for v in vertices:
            if not v[2] and v[1] < menor[1]:
                menor = (v[0], v[1])
        i = menor[0]
    
    caminho = []
    constroi_caminho(len(vertices) - 1, pais, set(), caminho)

    valor_caminho = 0
    i = 0
    while i < len(caminho) - 1:
        valor_caminho += matriz_adj_valorada[caminho[i]][caminho[i + 1]]
        i += 1
    return valor_caminho
