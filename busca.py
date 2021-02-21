from queue import priorityQueue
from expande import expande
from node import Node

def backtrace(nodo):
    trace = []
    actual = nodo
    while actual.pai != None:
        trace.append(actual.acao)
        actual = actual.pai
    trace.reverse()
    return trace

def bfs(nodo):
    explorados = []
    fronteira = [nodo]
    caminho = []
    while True:
        if not fronteira:
            return caminho

        actual = fronteira.pop(0)
        if actual.estado == '12345678_':
            return backtrace(actual)

        print(actual)
        if actual.estado not in explorados:
            explorados.append(actual.estado)
            fronteira.extend(expande(actual))
            caminho.append(actual.acao)

def dfs(nodo):
    explorados = []
    fronteira = [nodo]
    caminho = []
    while True:
        if not fronteira:
            return caminho

        actual = fronteira.pop()
        if actual.estado == '12345678_':
            return backtrace(actual)

        print(actual)
        if actual.estado not in explorados:
            explorados.append(actual.estado)
            fronteira.extend(expande(actual))
            caminho.append(actual.acao)

def astarHamming(nodo):
    explorados = []
    fronteira = PriorityQueue()
    fronteira.put((0, nodo))
    caminho = []
    while True:
        if not fronteira:
            return caminho

        actual = fronteira.get()
        if actual.estado == '12345678_':
            return backtrace(actual)

        print(actual)
        if actual.estado not in explorados:
            explorados.append(actual.estado)
            fronteira.extend(expande(actual))
            caminho.append(actual.acao)

def astarManhattan(nodo):
    explorados = []
    fronteira = PriorityQueue()
    fronteira.put((0, nodo))
    caminho = []
    while True:
        if not fronteira:
            return caminho

        actual = fronteira.get()
        if actual.estado == '12345678_':
            return backtrace(actual)

        print(actual)
        if actual.estado not in explorados:
            explorados.append(actual.estado)
            fronteira.extend(expande(actual))
            caminho.append(actual.acao)
