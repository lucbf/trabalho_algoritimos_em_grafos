from queue import Queue
from cores import Cores
from sys import maxsize

def calcula_fluxo_maximo(matriz_adj_valorada):
    ma = matriz_adj_valorada.copy()

    achou = True
    fluxo_maximo = 0
    while achou:
        fila = Queue()
        fila.put(0)
        fila2 = Queue()

        e = fila.get()
        fm = maxsize#fluxo máximo
        achou_ = False
        while e != len(ma) - 1:
            for idx, e_ in enumerate(ma[e]):
                if type(e_) != type(None):
                    fila2.put((e, idx))
                    fila.put(idx)
                    if fm > e_:
                        fm = e_
                    if idx == len(ma) -1:
                        achou_ = True
            e = fila.get()
        fluxo_maximo += fm
        if not achou_:
            achou = False
        else:
            while not fila2.empty():
                tupla = fila2.get()
                if ma[tupla[0]][tupla[1]] != None:
                    ma[tupla[0]][tupla[1]] -= fm
                if ma[tupla[0]][tupla[1]] == 0:
                    ma[tupla[0]][tupla[1]] = None
                if ma[tupla[1]][tupla[0]] == None:
                    ma[tupla[1]][tupla[0]] = fm
                else:
                    ma[tupla[1]][tupla[0]] += fm

    return fluxo_maximo        

