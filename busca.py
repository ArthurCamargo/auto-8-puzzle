from queue import PriorityQueue
from queue import SimpleQueue
from queue import LifoQueue 
from expande import expande
from node import Node
from dataclasses import dataclass, field
from typing import Any

#used to overcome the need to the data on the priority queue being used as explained here https://docs.python.org/3/library/queue.html
@dataclass(order=True)
class PriorityNode:
        priority: int
        item: Any=field(compare=False)

def hamming(nodo):
    string_perfeita = '12345678_'
    score = 0
    for i in range(len(nodo.estado)):
        if string_perfeita[i] != nodo.estado[i]:
            score += 1
    return score

def manhattan(nodo):
    string_perfeita = '12345678_'
    score = 0
    string_nodo = nodo.estado
    for i in range(len(string_nodo)):
        pos_perfeita = string_perfeita.find(string_nodo[i])
        pos_nodo = i
        #Vertical Distance
        score += abs(pos_nodo//3 - pos_perfeita//3)
        #Horizontal Distance
        score += abs(pos_nodo%3 - pos_perfeita%3)
    return score

#NODO
#|1|3|4|
#|6|7|8|
#|5|2|*|

#PERFEITO
#|1|2|3|
#|4|5|*|
#|7|8|6|

def backtrace(nodo):
    trace = []
    actual = nodo
    while actual.pai != None:
        trace.append(actual.acao)
        actual = actual.pai
    trace.reverse()
    return trace

def bfs(nodo):
    num_exp = 0
    explorados = []
    fronteira = SimpleQueue()
    fronteira.put(nodo)
    while True:
        if not fronteira:
            return []

        actual = fronteira.get()
        if actual.estado == '12345678_':
            print(num_exp, actual.custo)
            return backtrace(actual)

        if actual.estado not in explorados:
            explorados.append(actual.estado)
            for item in expande(actual):
                num_exp += 1
                item.custo = actual.custo + 1
                fronteira.put(item)

def dfs(nodo):
    num_exp = 0
    explorados = []
    fronteira = [nodo]
    while True:
        if not fronteira:
            return []

        actual = fronteira.pop()
        if actual.estado == '12345678_':
            print(num_exp, actual.custo)
            return backtrace(actual)

        if actual.estado not in explorados:
            explorados.append(actual.estado)
            for item in expande(actual):
                num_exp += 1
                item.custo = actual.custo + 1
                fronteira.append(item)

def astarHamming(nodo):
    num_exp = 0
    explorados = []
    fronteira = PriorityQueue()
    initial = PriorityNode(hamming(nodo), nodo)
    fronteira.put(initial)
    while True:
        if not fronteira:
            return []

        actual = fronteira.get()
        actual = actual.item
        if actual.estado == '12345678_':
            print(num_exp, actual.custo)
            return backtrace(actual)

        if actual.estado not in explorados:
            explorados.append(actual.estado)
            for item in expande(actual):
                num_exp += 1
                item.custo = actual.custo + 1
                priority = hamming(item) + item.custo
                new_item = PriorityNode(priority, item)
                fronteira.put(new_item)

def astarManhattan(nodo):
    num_exp = 0
    explorados = []
    fronteira = PriorityQueue()
    initial = PriorityNode(manhattan(nodo), nodo)
    fronteira.put(initial)
    while True:
        if not fronteira:
            return []

        actual = fronteira.get()
        actual = actual.item
        if actual.estado == '12345678_':
            print(num_exp, actual.custo)
            return backtrace(actual)

        if actual.estado not in explorados:
            explorados.append(actual.estado)
            for item in expande(actual):
                num_exp += 1
                item.custo = actual.custo + 1
                priority=manhattan(item) + item.custo
                new_item = PriorityNode(priority, item)
                fronteira.put(new_item)
