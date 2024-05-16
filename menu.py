from leitor_de_arquivo import LeitorDeArquivo
from matriz_adj import MatrizAdj
from lista_adj import ListaAdj

class Menu:
    lista_algoritimos = []

    def __init__(self, caminho_do_arquivo_a_ser_lido):
        leitor = LeitorDeArquivo(caminho_do_arquivo_a_ser_lido)
        tupla_vertices_arestas = leitor.interpretar()
        
        self.matriz_adj = MatrizAdj(tupla_vertices_arestas[0], tupla_vertices_arestas[1])
        self.lista_adj = ListaAdj(tupla_vertices_arestas[0], tupla_vertices_arestas[1])

    def menu_representacoes(self):
        while True:
            print("Ver matriz de adjacência do grafo [1]")
            print("Ver lista de adjacência do grafo [2]")

            resposta = int(input())
            if resposta == 1:
                print(self.matriz_adj)
                break
            elif resposta == 2:
                print(self.lista_adj)
                break
    
    def executar(self):
        print("Representações [1]")

        resposta = int(input())
        if resposta == 1:
            self.menu_representacoes()