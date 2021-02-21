import sys, os
from sucessor import sucessor
from expande import expande
from node import Node
from busca import *


#TODO:
# 1 Sucessor OK
# 2 Expande + Nodes OK
# 3 Busca no Grafo 

def main():

    argc = len(sys.argv)

    if argc != 3:
        print("Usage <", sys.argv[0], "> estado initial_cost")
        os.strerror(1)
    initial_state = sys.argv[1]
    initial_cost = sys.argv[2]

    initial_node = Node(None, initial_state, initial_cost,
                        acao='')
    caminho = bfs(initial_node)
    print(*caminho)

if __name__ == "__main__":
    main()
