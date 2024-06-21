from time import perf_counter_ns
from leitor_de_arquivo import LeitorDeArquivo
from matriz_adj import MatrizAdj
from lista_adj import ListaAdj
from erro import imprimir_erro
from verificacoes.qtd import conta
from verificacoes.grau import calcula_grau
from verificacoes.conexidade_forte import gerar_lista_conexidade_forte

class Menu:
    lista_algoritimos = []

    def __init__(self, caminho_do_arquivo_a_ser_lido):
        leitor = LeitorDeArquivo(caminho_do_arquivo_a_ser_lido)
        tupla_vertices_arestas = leitor.interpretar()


        print("O grafo é direcionado? [S/N]", end = ' ')
        resposta = input().lower()

        if resposta == 's':
            self.direcionado = True
        else:
            self.direcionado = False

        
        self.matriz_adj = MatrizAdj(tupla_vertices_arestas[0], tupla_vertices_arestas[1], self.direcionado)
        self.lista_adj = ListaAdj(tupla_vertices_arestas[0], tupla_vertices_arestas[1], self.direcionado)
        self.informacao_arquivo = (caminho_do_arquivo_a_ser_lido, tupla_vertices_arestas)

    def menu_representacoes(self):
        tempo = 0
        while True:
            print("[1] Ver matriz de adjacência do grafo")
            print("[2] Ver lista de adjacência do grafo")

            resposta = int(input())
            tempo = perf_counter_ns()
            if resposta == 1:
                print(self.matriz_adj)
                break
            elif resposta == 2:
                print(self.lista_adj)
                break
        return perf_counter_ns() - tempo
        
    
    def menu_manipulacoes(self):
        tipo_grafo = ""
        if self.direcionado:
            tipo_grafo = "Direcionado"
        else:
            tipo_grafo = "Não Direcionado"

        print("Grafo {}: V = ".format(tipo_grafo), end='')
        print(self.informacao_arquivo[1][0], end="; A = ")
        print(self.informacao_arquivo[1][1], end=';\n')

        
        tempo = 0
        while True:
            print("[1] Adicionar vértice no grafo")
            print("[2] Remover vértice no grafo")
            print("[3] Adicionar aresta no grafo")
            print('[4] Remover aresta do grafo')

            resposta = int(input())

            if resposta == 1:
                print("Qual o vértice a ser adicionado?", end=' ')
                vertice = int(input())

                tempo = perf_counter_ns()

                if vertice in self.informacao_arquivo[1][0]:
                    imprimir_erro("Vértice já existe no grafo.")
                else:
                    self.informacao_arquivo[1][0].append(vertice)
                break
            if resposta == 2:
                print("Qual o vértice a ser removido?", end=' ')
                vertice = int(input())

                tempo = perf_counter_ns()

                if vertice in self.informacao_arquivo[1][0]:
                    self.informacao_arquivo[1][0].remove(vertice)

                    i = len(self.informacao_arquivo[1][1]) - 1
                    while i >= 0:
                        if self.informacao_arquivo[1][1][i][0] == vertice or self.informacao_arquivo[1][1][i][1] == vertice:
                            del self.informacao_arquivo[1][1][i]
                        i -= 1
                else:
                    imprimir_erro("Vértice não existe no grafo.")
                break
            if resposta == 3:
                print("Qual a aresta a ser adicionada? [_ _]", end=' ')
                aresta = input().split(' ')

                tempo = perf_counter_ns()

                aresta[0] = int(aresta[0])
                aresta[1] = int(aresta[1])
                aresta = (aresta[0], aresta[1])
                if aresta in self.informacao_arquivo[1][1]:
                    imprimir_erro("Aresta já existe no grafo.")
                else:
                    self.informacao_arquivo[1][1].append(aresta)
                break
            if resposta == 4:
                print("Qual a aresta a ser removida? [_ _]", end=' ')
                aresta = input().split(' ')

                tempo = perf_counter_ns()

                aresta[0] = int(aresta[0])
                aresta[1] = int(aresta[1])
                aresta = (aresta[0], aresta[1])
                if aresta in self.informacao_arquivo[1][1]:
                    self.informacao_arquivo[1][1].remove(aresta)
                else:
                    imprimir_erro("Aresta não existe no grafo.")
                break
        self.atualizar_arquivo()
        self.matriz_adj = MatrizAdj(self.informacao_arquivo[1][0], self.informacao_arquivo[1][1], self.direcionado)
        self.lista_adj = ListaAdj(self.informacao_arquivo[1][0], self.informacao_arquivo[1][1], self.direcionado)

        return perf_counter_ns() - tempo
    

    def atualizar_arquivo(self):
        string = 'V = {'
        for v in self.informacao_arquivo[1][0]:
            string += str(v)
            string += ','
        string = list(string)
        string[-1] = '}'
        string = "".join(string)
        
        string += '; A = {'

        for a in self.informacao_arquivo[1][1]:
            string += '('
            string += str(a[0])
            string += ','
            string += str(a[1])
            string += '),'
        string = list(string)
        string[-1] = '}'
        string = "".join(string)
        string += ';'

        aq = open(self.informacao_arquivo[0], 'w')
        aq.write(string)
        aq.close()


    def menu_verificacoes(self):
        tempo = 0
        while True:
            print("[1] Contar quantos vértices tem no grafo")
            print("[2] Contar quantas arestas tem no grafo")
            print("[3] Calcular o grau de um vértice")
            id = 4
            if self.direcionado:
                print("[4] Verificar as conexidades fortes do grafo")
                id = 5
            

            entrada = int(input())
            tempo = perf_counter_ns()

            if entrada == 1:
                nv = conta(self.informacao_arquivo[1][0])
                print("O grafo tem {} vértices".format(nv))
                break
            elif entrada == 2:
                na = conta(self.informacao_arquivo[1][1])
                print("O grafo tem {} arestas".format(na))
                break
            elif entrada == 3:
                print("Qual o vértice a ser analisado?", end=' ')
                vertice = int(input())
                tempo = perf_counter_ns()

                tam = 0
                for _ in self.matriz_adj.matriz_adj:
                    tam += 1
                
                if tam - 1 < vertice or vertice < 0:
                    print("Vértice inválido.")
                else:
                    grau = calcula_grau(vertice, self.lista_adj.lista_adj)
                    print("O grau do vértice {} é {}.".format(vertice, grau))
                break
            elif entrada == 4 and self.direcionado:
                lista = gerar_lista_conexidade_forte(self.matriz_adj.matriz_adj)
                print("Os vértices de conexidade forte são: {}".format(lista))
                break


        return perf_counter_ns() - tempo
    
    def executar(self):
        sair = False

        tempo = 0

        while not sair:
            if tempo != 0:
                print("O tempo de execução foi de: {}ns".format(tempo))


            print("[1] Representações")
            print("[2] Manipular Grafo")
            print("[3] Verificações")
            print("[20] Sair do programa")

            resposta = int(input())
            if resposta == 1:
                tempo = self.menu_representacoes()
            elif resposta == 2:
                tempo = self.menu_manipulacoes()
            elif resposta == 3:
                tempo = self.menu_verificacoes()
            elif resposta == 20:
                sair = True