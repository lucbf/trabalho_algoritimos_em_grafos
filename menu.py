
from leitor_de_arquivo import LeitorDeArquivo
from matriz_adj import MatrizAdj, MatrizAdjValorada
from lista_adj import ListaAdj, ListaAdjValorada
from bipartido import verifica_bipartido
from ciclos import verificar_ciclos
from conexo import verifica_conexo
from ordem_topologica import gera_ordem_topologica
from bfs import gerar_arvore_bfs
from dfs import gerar_arvore_dfs
from comp_conexos import comp_conexos
from comp_fortemente_conexas import lista_comp_fortemente_conexas
from caminho_euleriano import verifica_pseudosimetrico, gerar_caminho_euleriano
from geradora_minima import kruskal

class Menu:
    lista_algoritimos = []

    def __init__(self, caminho_do_arquivo_a_ser_lido):
        leitor = LeitorDeArquivo(caminho_do_arquivo_a_ser_lido)
        tupla_vertices_arestas_direcionado = leitor.interpretar()

        self.direcionado = tupla_vertices_arestas_direcionado[2]
        self.matriz_adj = MatrizAdj(tupla_vertices_arestas_direcionado[0], tupla_vertices_arestas_direcionado[1])
        self.lista_adj = ListaAdj(tupla_vertices_arestas_direcionado[0], tupla_vertices_arestas_direcionado[1])
        self.lista_adj_valorada = ListaAdjValorada(tupla_vertices_arestas_direcionado[0], tupla_vertices_arestas_direcionado[1])
        self.matriz_adj_valorada = MatrizAdjValorada(tupla_vertices_arestas_direcionado[0], tupla_vertices_arestas_direcionado[1])
        self.informacao_arquivo = (caminho_do_arquivo_a_ser_lido, tupla_vertices_arestas_direcionado)

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

        while not sair:
            print("Verificar")
            print("[1] Conexo")
            print("[2] Bipartido")
            print("[3] Euleriano")
            print("[4] Possui ciclo")
            print("Listar")
            print("[5] Componentes conexas")
            print("[6] Componentes fortemente conexas")
            print("[7] Caminho euleriano")
            print("[8] Caminho Hamiltoniano")
            print("[9] Vértices de articulação")
            print("[10] Arestas ponte")
            print("Gerar")
            print("[11] Árvore de profundidade")
            print("[12] Árvore de largura")
            print("[13] Árvore geradora mínima")
            print("[14] Ordem topológica")
            print("[15] Valor do caminho mínimo entre dois vértices")
            print("[16] Valor do fluxo máximo")
            print("[17] Fecho transitivo")
            print("Insira [18] para sair")
                  

            resposta = int(input())
            if resposta == 1:
                self.imprimir_booleano(verifica_conexo(self.lista_adj.lista_adj))
            elif resposta == 2:
                self.imprimir_booleano(verifica_bipartido(self.lista_adj.lista_adj))
            elif resposta == 3:
                self.imprimir_booleano(verifica_pseudosimetrico(self.lista_adj.lista_adj, self.direcionado))
            elif resposta == 4:
                self.imprimir_booleano(verificar_ciclos(self.lista_adj.lista_adj))
            elif resposta == 5:
                self.imprimir_multiplas_listas(comp_conexos(self.lista_adj.lista_adj))
            elif resposta == 6:
                self.imprimir_multiplas_listas(lista_comp_fortemente_conexas(self.matriz_adj.matriz_adj))
            elif resposta == 7:
                self.imprimir_lista(gerar_caminho_euleriano(self.lista_adj.lista_adj, self.direcionado))
            elif resposta == 11:
                self.imprimir_lista(gerar_arvore_dfs(self.lista_adj.lista_adj))
            elif resposta == 12:
                self.imprimir_lista(gerar_arvore_bfs(self.lista_adj.lista_adj))
            elif resposta == 13:
                print(kruskal(self.informacao_arquivo[1][1], len(self.matriz_adj.matriz_adj), self.direcionado))
            elif resposta == 14 and self.direcionado == True:
                self.imprimir_lista(gera_ordem_topologica(self.lista_adj.lista_adj))
            elif resposta == 18:
                sair = True