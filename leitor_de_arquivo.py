import os.path
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