
from leitor_de_arquivo import LeitorDeArquivo
from matriz_adj import MatrizAdj
from lista_adj import ListaAdj
from verificacoes.bipartido import verifica_bipartido
from verificacoes.ciclos import verificar_ciclos
from verificacoes.euleriano import verifica_euleriano
from verificacoes.conexo import verifica_conexo

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

    
    def executar(self):
        sair = False

        while not sair:
            if tempo != 0:
                print("O tempo de execução foi de: {}ns".format(tempo))


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
                print(verifica_conexo(self.lista_adj.lista_adj))
            elif resposta == 2:
                print(verifica_bipartido(self.lista_adj.lista_adj))
            elif resposta == 3:
                print(verifica_euleriano(self.lista_adj.lista_adj))
            elif resposta == 4:
                print(verificar_ciclos(self.lista_adj.lista_adj))
            elif resposta == 18:
                sair = True