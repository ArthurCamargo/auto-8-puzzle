import sys, os
from sucessor import sucessor
from expande import expande
from node import Node
from busca import *


#TODO:
# 1 Sucessor OK TESTADA
# 2 Expande + Nodes OK TESTADO
# 3 Busca no Grafo 


def main():

    argc = len(sys.argv)

    if sys.argv[1] == '-s' and argc == 3:
        estado = sys.argv[2]
        suc = sucessor(estado)
        str = ''
        for i in suc:
            str += '('
            i = ','.join(i)
            str += i
            str += ') '
        str.rstrip()
        print(str)

    elif sys.argv[1] == '-e' and argc == 4:
        ini_state = sys.argv[2]
        ini_cost = sys.argv[3]
        ini_node = Node(estado=ini_state, custo=ini_cost)
        new_node = expande(ini_node)
        print(*new_node)
    elif sys.argv[1] == '-r' and argc == 4:
        ini_state = sys.argv[3]
        ini_node = Node(estado=ini_state)
        if sys.argv[2] == '-bfs':
            print(*bfs(ini_node))
        elif sys.argv[2] == '-dfs':
            print(*dfs(ini_node))
        elif sys.argv[2] == '-as1':
            print(*astarHamming(ini_node))
        elif sys.argv[2] == '-as2':
            print(*astarManhattan(ini_node))

if __name__ == "__main__":
    main()
