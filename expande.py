from sucessor import sucessor
from node import Node

def expande(node):
    """ Expande o grafo de estados do game"""
    novos_nodes = []
    if node.estado != None:
        novos_estados = sucessor(node.estado)

        for direcao, estado in novos_estados:
            new_node = Node(node, estado, int(node.custo) + 1, direcao)
            node.filhos.append(new_node)
            novos_nodes.append(new_node)
    return novos_nodes
