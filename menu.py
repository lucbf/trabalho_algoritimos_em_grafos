from leitor_de_arquivo import LeitorDeArquivo
from matriz_adj import MatrizAdj
from lista_adj import ListaAdj
from erro import imprimir_erro

class Menu:
    lista_algoritimos = []

    def __init__(self, caminho_do_arquivo_a_ser_lido):
        leitor = LeitorDeArquivo(caminho_do_arquivo_a_ser_lido)
        tupla_vertices_arestas = leitor.interpretar()
        
        self.matriz_adj = MatrizAdj(tupla_vertices_arestas[0], tupla_vertices_arestas[1])
        self.lista_adj = ListaAdj(tupla_vertices_arestas[0], tupla_vertices_arestas[1])
        self.informacao_arquivo = (caminho_do_arquivo_a_ser_lido, tupla_vertices_arestas)

    def menu_representacoes(self):
        while True:
            print("[1] Ver matriz de adjacência do grafo")
            print("[2] Ver lista de adjacência do grafo")

            resposta = int(input())
            if resposta == 1:
                print(self.matriz_adj)
                break
            elif resposta == 2:
                print(self.lista_adj)
                break
    
    def menu_manipulacoes(self):
        print("Grafo: V = ", end='')
        print(self.informacao_arquivo[1][0], end="; A = ")
        print(self.informacao_arquivo[1][1], end=';\n')

        

        while True:
            print("[1] Adicionar vértice no grafo")
            print("[2] Remover vértice no grafo")
            print("[3] Adicionar aresta no grafo")
            print('[4] Remover aresta do grafo')

            resposta = int(input())

            if resposta == 1:
                print("Qual o vértice a ser adicionado?", end=' ')
                vertice = int(input())
                if vertice in self.informacao_arquivo[1][0]:
                    imprimir_erro("Vértice já existe no grafo.")
                else:
                    self.informacao_arquivo[1][0].append(vertice)
                break
            if resposta == 2:
                print("Qual o vértice a ser removido?", end=' ')
                vertice = int(input())
                if vertice in self.informacao_arquivo[1][0]:
                    self.informacao_arquivo[1][0].remove(vertice)

                    for idx, e in enumerate(self.informacao_arquivo[1][1]):
                        if e[0] == vertice or e[1] == vertice:
                            del self.informacao_arquivo[1][1][idx]
                else:
                    imprimir_erro("Vértice não existe no grafo.")
                break
            if resposta == 3:
                print("Qual a aresta a ser adicionada? [_ _]", end=' ')
                aresta = input().split(' ')
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
                aresta[0] = int(aresta[0])
                aresta[1] = int(aresta[1])
                aresta = (aresta[0], aresta[1])
                if aresta in self.informacao_arquivo[1][1]:
                    self.informacao_arquivo[1][1].remove(aresta)
                else:
                    imprimir_erro("Aresta não existe no grafo.")
                break
        self.atualizar_arquivo()
        self.matriz_adj = MatrizAdj(self.informacao_arquivo[1][0], self.informacao_arquivo[1][1])
        self.lista_adj = ListaAdj(self.informacao_arquivo[1][0], self.informacao_arquivo[1][1])
    

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


            
    
    def executar(self):
        sair = False

        while not sair:
            print("[1] Representações")
            print("[2] Manipular Grafo")
            print("[20] Sair do programa")

            resposta = int(input())
            if resposta == 1:
                self.menu_representacoes()
            elif resposta == 2:
                self.menu_manipulacoes()
            elif resposta == 20:
                sair = True