import os.path
from enum import Enum
from erro import imprimir_erro

class LeitorDeArquivo:
    '''
        Verifica se o caminho para o arquivo é
        válido. Se não for, imprime uma mensagem
        de erro e fecha o programa

        Caso seja um arquivo válido self.arquivo = arquivo
    '''
    def __init__(self, arquivo):
        if os.path.isfile(arquivo):
            self.arquivo = arquivo
        else:
            imprimir_erro(arquivo + " não é um arquivo.")

    '''
    Lê arquivo e retorna os vértices e as arestas
    '''
    def interpretar(self):
        aq_ = open(self.arquivo)
        aq = aq_.read()
        aq_.close()

        vertices = []
        arestas = []

        Modo = Enum('Modo', ['NENHUM', 'VERTICE', 'TRANSICAO', 'ARESTA', 'FIM'])
        modo = Modo.NENHUM

        comeca = -1

        aresta_v1 = -1
        aresta_v2 = -1
        for idx, char in enumerate(aq):
            if modo == Modo.NENHUM:
                if idx == 0 and char != 'V':
                    imprimir_erro("Caractere inválido no arquivo.")
                elif (idx == 1 or idx == 3) and char != ' ':
                    imprimir_erro("Caractere inválido no arquivo.")
                elif idx == 2 and char != '=':
                    imprimir_erro("Caractere inválido no arquivo.")
                elif idx == 4:
                    if char != '{':
                        imprimir_erro("Caractere inválido no arquivo.")
                    else:
                        modo = Modo.VERTICE
            elif modo == Modo.VERTICE:
                if idx % 2:
                    vertices.append(int(char))
                elif char != ',':
                    if char == '}':
                        modo = Modo.TRANSICAO
                        comeca = idx + 1
                    else:
                        imprimir_erro("Caractere inválido no arquivo.")
            elif modo == Modo.TRANSICAO:
                idx_transicao = idx - comeca

                if idx_transicao == 0 and char != ';':
                    imprimir_erro("Caractere inválido no arquivo.")
                elif idx_transicao % 2 and char != ' ':
                    imprimir_erro("Caractere inválido no arquivo.")
                elif idx_transicao == 2 and char != 'A':
                    imprimir_erro("Caractere inválido no arquivo.")
                elif idx_transicao == 4 and char != '=':
                    imprimir_erro("Caractere inválido no arquivo.")
                elif idx_transicao == 6:
                    if char == '{':
                        modo = Modo.ARESTA
                        comeca = idx + 1
                    else:
                        imprimir_erro("Caractere inválido no arquivo.")
            elif modo == Modo.ARESTA:
                if char == '}':
                    modo = Modo.FIM
                else:
                    idx_aresta = idx - comeca
                    if idx_aresta == 0 and char != '(':
                        imprimir_erro("Caractere inválido no arquivo.")
                    elif idx_aresta == 1:
                        aresta_v1 = int(char)
                    elif idx_aresta == 2 and char != ',':
                        imprimir_erro("Caractere inválido no arquivo.")
                    elif idx_aresta == 3:
                        aresta_v2 = int(char)
                    elif idx_aresta == 4:
                        if char == ')':
                            if aresta_v1 in vertices and aresta_v2 in vertices:
                                arestas.append((aresta_v1, aresta_v2))
                            else:
                                imprimir_erro("Aresta do arquivo se conecta a vértice inexistente.")
                        else:
                            imprimir_erro("Caractere inválido no arquivo.")
                    elif idx_aresta == 5:
                        if char == ',':
                            comeca = idx + 1
                        else:
                            imprimir_erro("Caractere inválido no arquivo.")
        return (vertices, arestas)

