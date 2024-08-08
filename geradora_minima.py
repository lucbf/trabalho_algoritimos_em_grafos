def kruskal(arestas, nvertices, direcionado):
    if direcionado:
        return "-1"

    ar = arestas.copy()
    ar.sort(key=lambda a: a[2])
    retorno = "{},{}".format(ar[0][0], ar[0][1])
    vertices_adicionados = set([ar[0][0], ar[0][1]])
    i = 1
    j = 1
    while i < nvertices - 1:
        if not ar[j][0] in vertices_adicionados:
            i += 1
            retorno += " {},{}".format(ar[j][0], ar[j][1])
            vertices_adicionados.add(ar[j][0])

            if not ar[j][1] in vertices_adicionados:
                i += 1
                vertices_adicionados.add(ar[j][1])
        elif not ar[j][1] in vertices_adicionados:
            i += 1
            retorno += " {},{}".format(ar[j][0], ar[j][1])
            vertices_adicionados.add(ar[j][1])
        j += 1
    return retorno
