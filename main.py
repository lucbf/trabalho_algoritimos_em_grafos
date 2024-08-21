from enum import Enum

class Cores(Enum):
    BRANCO = 0
    CINZA = 1
    PRETO = 2
class LeitorDeArquivo:
    def interpretar(self):

        aq = [input(), input()]

        vertices = []
        arestas = []

        linha1 = aq[0].split(' ')
        nvertices = int(linha1[0])
        narestas = int(linha1[1])

        direcionado = False
        if aq[1] == 'direcionado':
            direcionado = True

        for i in range(narestas):
            aq.append(input())

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
        
        arestas.sort()
        
        for n in range(nvertices):
            vertices.append(n)
        return (vertices, arestas, direcionado)

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


def dfs_conexo(lista_adj, idx, cores):
    cores[idx] = Cores.CINZA

    for e in lista_adj[idx]:
        if cores[e] == Cores.BRANCO:
            dfs_conexo(lista_adj, e, cores)

    cores[idx] = Cores.PRETO


def verifica_conexo(lista_adj):
    tam = 0
    for _ in lista_adj:
        tam += 1

    cores = [Cores.BRANCO for _ in range(tam)]

    dfs_conexo(lista_adj, 0, cores)

    for c in cores:
        if c != Cores.PRETO:
            return False
    else:
        return True


def dfs_bipartido(lista_adj, cores, idx, cor_atual = Cores.CINZA, bipartido = True):
    cores[idx] = cor_atual

    for v in lista_adj[idx]:
        if cores[v] == cor_atual:
            bipartido = False
            break
        elif cores[v] == Cores.BRANCO:
            cor = Cores.BRANCO
            if cor_atual == Cores.CINZA:
                cor = Cores.PRETO
            else:
                cor = Cores.PRETO
            bipartido = dfs_bipartido(lista_adj, cores, v, cor, bipartido)
            if bipartido == False:
                break
    
    return bipartido

def verifica_bipartido(lista_adj):

    tam = 0
    for i in lista_adj:
        tam += 1

    cores = [Cores.BRANCO for _ in range(tam)]
    
    bipartido = True
    for idx, c in enumerate(cores):
        if c == Cores.BRANCO:
            bipartido = dfs_bipartido(lista_adj, cores, idx)
            if not bipartido:
                break
    
    return bipartido


def encontra_ciclo(lista_adj, idx, idx_inicial, arestas_visitadas, caminho, direcionado):
    caminho.append(idx)

    for e in lista_adj[idx]:
        if not ((idx, e) in arestas_visitadas) or (not direcionado and not ((e, idx) in arestas_visitadas)):
            arestas_visitadas.add((idx, e))
            if not direcionado:
                arestas_visitadas.add((e, idx))
            if e == idx_inicial or encontra_ciclo(lista_adj, e, idx_inicial, arestas_visitadas, caminho, direcionado):
                return True
            
    return False

def calcula_grau_balanceado(lista_adj, v):
    grau = 0
    for a in lista_adj:
        for b in a:
            if b == v:
                grau += 1
    for _ in lista_adj[v]:
        grau -= 1

def calcula_grau(lista_adj, v):
    grau = 0
    for _ in lista_adj[v]:
        grau += 1
    
    return grau

def verifica_pseudosimetrico(lista_adj, direcionado):
    if direcionado:
        for idx in range(len(lista_adj)):
            if calcula_grau_balanceado(lista_adj, idx) != 0:
                return False
    else:
        for idx in range(len(lista_adj)):
            if calcula_grau(lista_adj, idx) % 2 == 1:
                return False
    return True

def gerar_caminho_euleriano(lista_adj, direcionado):
    i = 0
    if not verifica_pseudosimetrico(lista_adj, direcionado):
        return []
    
    arestas_visitadas = []
    caminho = set()
    while i < len(lista_adj):
        c = []
        if not encontra_ciclo(lista_adj, i, i, arestas_visitadas, c, direcionado):
            i += 1
        else:
            if caminho != []:
                for idx, cam in caminho:
                    if cam == i:
                        del caminho[idx]
                        c.reverse()
                        for e in c:
                            caminho.insert(idx, e)
            else:
                caminho = c
    
    return caminho


def dfs_ciclo(lista_adj, idx, cores, achou_ciclo = False):
    cores[idx] = Cores.CINZA

    for v in lista_adj[idx]:
        if cores[v] == Cores.BRANCO:
            achou_ciclo = dfs_ciclo(lista_adj, v, cores, achou_ciclo)
            if achou_ciclo:
                break
        else:
            achou_ciclo = True
            break
    
    cores[idx] = Cores.PRETO
    return achou_ciclo

def verificar_ciclos(lista_adj):
    ciclos = False
    
    cores = [Cores.BRANCO for _ in range(len(lista_adj))]

    for idx, c in enumerate(cores):
        if c == Cores.BRANCO:
            ciclos = dfs_ciclo(lista_adj, idx, cores)
            if ciclos:
                break
    return ciclos


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
            fila = Queue()
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



class Ordem:
    def __init__(self) -> None:
        self.entrada = -1
        self.saida = -1

def dfs_ida(matriz_adj, idx, e_s, tempo):
    e_s[idx].entrada = tempo

    for i in matriz_adj[idx]:
        if i == 1 and e_s[i].entrada == -1:
            tempo = dfs_ida(matriz_adj, i, e_s, tempo + 1)
    
    tempo += 1
    e_s[idx].saida = tempo

    return tempo

def dfs_volta(matriz_adj, idx, cores):
    cores[idx] = Cores.CINZA

    i = 0
    while i < len(matriz_adj):
        if matriz_adj[i][idx] == 1 and cores[i] == Cores.BRANCO:
            dfs_volta(matriz_adj, i, cores)
        i += 1
    cores[idx] = Cores.PRETO

def lista_comp_fortemente_conexas(matriz_adj):
    e_s = [Ordem() for _ in range(len(matriz_adj))]
    cores = [Cores.BRANCO for _ in range(len(matriz_adj))]
    tempo = 1
    for idx, c in enumerate(cores):
        if c == Cores.BRANCO:
            tempo = dfs_ida(matriz_adj, idx, e_s, tempo)

    cores = [Cores.BRANCO for _ in range(len(matriz_adj))]
    componentes = 0
    while Cores.BRANCO in cores:
        maior = (0, 0)
        for idx, v in enumerate(e_s):
            if cores[idx] == Cores.BRANCO and v.saida > maior[1]:
                maior = (idx, v.saida)
        dfs_volta(matriz_adj, maior[0], cores)
        componentes += 1
    
    return componentes

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
            fila = Queue()#excluindo vértice atual e o vértice analisado
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
import sys
def dfs_ponte(lista_adj, idx, idx_anterior, tempo, tempos, indicadores, arestas_ponte):
    tempo += 1
    tempos[idx] = tempo
    indicadores[idx] = tempo

    for v in lista_adj[idx]:
        if tempos[v] == sys.maxsize:
            indicadores[idx] = min(dfs_ponte(lista_adj, v, idx, tempo, tempos, indicadores, arestas_ponte), indicadores[idx])
            if indicadores[v] > indicadores[idx]:
                arestas_ponte[0] += 1
        elif v != idx_anterior:
            indicadores[idx] = indicadores[v]
    
    return indicadores[idx]


def qtd_arestas_ponte(lista_adj, direcionado):
    if direcionado:
        return "-1"
    tempos = [sys.maxsize for _ in range(len(lista_adj))]
    indicadores = tempos.copy()
    arestas_ponte = [0]

    for idx, t in enumerate(tempos):
        if t == sys.maxsize:
            dfs_ponte(lista_adj, idx, -1, 0, tempos, indicadores, arestas_ponte)
    
    return arestas_ponte[0]
    


def dfs(lista_adj, idx, cores, arvore):
    cores[idx] = Cores.CINZA
    arvore.append(idx)

    for e in lista_adj[idx]:
        if cores[e] == Cores.BRANCO:
            dfs(lista_adj, e, cores, arvore)
    
    cores[idx] = Cores.PRETO

def gerar_arvore_dfs(lista_adj):
    arvore = []

    tam = 0
    for _ in lista_adj:
        tam += 1

    cores = [Cores.BRANCO for _ in range(tam)]

    dfs(lista_adj, 0, cores, arvore)
    
    return arvore


def gerar_arvore_bfs(lista_adj):

    cores = [Cores.BRANCO for _ in range(len(lista_adj))]

    fila = [0]
    for i in fila:
        cores[i] = Cores.CINZA

        for j in lista_adj[i]:
            if cores[j] == Cores.BRANCO and not (j in fila):
                fila.append(j)
        cores[i] = Cores.PRETO
    
    return fila
def kruskal(arestas, nvertices, direcionado):
    if direcionado:
        return "-1"

    ar = arestas.copy()
    ar.sort(key=lambda a: a[2])
    retorno = 0
    vertices_adicionados = set([ar[0][0], ar[0][1]])
    i = 1
    j = 1
    while i < nvertices - 1:
        if not ar[j][0] in vertices_adicionados:
            i += 1
            retorno += ar[j][2]
            vertices_adicionados.add(ar[j][0])

            if not ar[j][1] in vertices_adicionados:
                i += 1
                vertices_adicionados.add(ar[j][1])
        elif not ar[j][1] in vertices_adicionados:
            i += 1
            retorno += ar[j][2]
            vertices_adicionados.add(ar[j][1])
        j += 1
    return retorno

def dfs_ot(lista_adj, idx, cores, ordem = []):
    cores[idx] = Cores.CINZA

    for e in enumerate(lista_adj[idx]):
        if cores[e] == Cores.BRANCO:
            dfs_ot(lista_adj, e, cores)

    cores[idx] = Cores.PRETO
    ordem.insert(0, idx)


def gera_ordem_topologica(lista_adj):
    tam = 0
    for _ in lista_adj:
        tam += 1
    
    cores = [Cores.BRANCO for _ in range(tam)]
    ordem = []

    for idx, c in enumerate(cores):
        if c == Cores.BRANCO:
            dfs_ot(lista_adj, idx, cores, ordem)
    
    return ordem

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
from sys import maxsize

def calcula_fecho_transitivo(matriz_adj):
    #prepara matriz de adjacência
    ma = []
    for lista in matriz_adj:
        ma.append([])
        for i, e in enumerate(lista):
            if e == 0:
                ma[-1].append(maxsize)
            else:
                ma[-1].append(i)
    for i in range(len(ma)):
        ma[i][i] = i

    #floyd-warshall
    for k in range(len(ma)):
        for i in range(len(ma)):
            for j in range(len(ma)):
                if ma[i][k] + ma[k][j] < ma[i][j]:
                    ma[i][j] = j
    
    for e in ma[0]:
        if e >= maxsize:
            del e
    
    return ma[0]

class Menu:

    def __init__(self):
        self.lista_algoritimos = input().split(' ')
        leitor = LeitorDeArquivo()
        tupla_vertices_arestas_direcionado = leitor.interpretar()

        self.direcionado = tupla_vertices_arestas_direcionado[2]
        self.matriz_adj = MatrizAdj(tupla_vertices_arestas_direcionado[0], tupla_vertices_arestas_direcionado[1])
        self.lista_adj = ListaAdj(tupla_vertices_arestas_direcionado[0], tupla_vertices_arestas_direcionado[1])
        self.lista_adj_valorada = ListaAdjValorada(tupla_vertices_arestas_direcionado[0], tupla_vertices_arestas_direcionado[1])
        self.matriz_adj_valorada = MatrizAdjValorada(tupla_vertices_arestas_direcionado[0], tupla_vertices_arestas_direcionado[1])
        self.informacao_arquivo = ('', tupla_vertices_arestas_direcionado)

    def imprimir_lista(self, lista):
        if len(lista) > 0:
            print(lista[0], end='')
        i = 1
        while i < len(lista):
            print(' {}'.format(lista[i]), end='')
            i += 1
        print()

    def imprimir_multiplas_listas(self, listas):
        if len(listas) > 0:
            print(listas[0][0], end='')

            i = 1
            while i < len(listas[0]):
                print(" {}".format(listas[0][i]), end='')
                i += 1
            
            i = 1
            while i < len(listas):
                print(" - ", end='')
                for v in listas[i]:
                    print(" {}".format(v), end='')
                i += 1
        print()

    def imprimir_booleano(self, b):
        if b:
            print(1)
        else:
            print(0)

    def executar(self):
        sair = False

        for resposta in self.lista_algoritimos:
            '''
            print("Verificar")
            print("[1] Conexo")
            print("[2] Bipartido")
            print("[3] Euleriano")
            print("[4] Possui ciclo")
            print("Listar")
            print("[5] Componentes conexas")
            print("[6] Componentes fortemente conexas")
            print("[7] Vértices de articulação")
            print("[8] Arestas ponte")
            print("Gerar")
            print("[9] Árvore de profundidade")
            print("[10] Árvore de largura")
            print("[11] Árvore geradora mínima")
            print("[12] Ordem topológica")
            print("[13] Valor do caminho mínimo entre dois vértices")
            print("[14] Valor do fluxo máximo")
            print("[15] Fecho transitivo")
            print("[16] Caminho euleriano")
            print("Insira [17] para sair")
            '''
            resposta = int(resposta)
            if resposta == 1:
                self.imprimir_booleano(verifica_conexo(self.lista_adj.lista_adj))
            elif resposta == 2:
                self.imprimir_booleano(verifica_bipartido(self.lista_adj.lista_adj))
            elif resposta == 3:
                self.imprimir_booleano(verifica_pseudosimetrico(self.lista_adj.lista_adj, self.direcionado))
            elif resposta == 4:
                self.imprimir_booleano(verificar_ciclos(self.lista_adj.lista_adj))
            elif resposta == 5:
                print(comp_conexos(self.lista_adj.lista_adj))
            elif resposta == 6:
                print(lista_comp_fortemente_conexas(self.matriz_adj.matriz_adj))
            elif resposta == 16:
                self.imprimir_lista(gerar_caminho_euleriano(self.lista_adj.lista_adj, self.direcionado))
            elif resposta == 7:
                self.imprimir_lista(vertices_articulacao(self.lista_adj.lista_adj, self.direcionado))
            elif resposta == 8:
                print(qtd_arestas_ponte(self.lista_adj.lista_adj, self.direcionado))
            elif resposta == 9:
                self.imprimir_lista(gerar_arvore_dfs(self.lista_adj.lista_adj))
            elif resposta == 10:
                self.imprimir_lista(gerar_arvore_bfs(self.lista_adj.lista_adj))
            elif resposta == 11:
                print(kruskal(self.informacao_arquivo[1][1], len(self.matriz_adj.matriz_adj), self.direcionado))
            elif resposta == 12 and self.direcionado == True:
                self.imprimir_lista(gera_ordem_topologica(self.lista_adj.lista_adj))
            elif resposta == 13:
                print(dijkstra(self.lista_adj_valorada.lista_adj, self.matriz_adj_valorada.matriz_adj))
            elif resposta == 14:
                print(-1)
            elif resposta == 15:
                self.imprimir_lista(calcula_fecho_transitivo(self.matriz_adj.matriz_adj))
            elif resposta == 17:
                sair = True

menu = Menu()
menu.executar()