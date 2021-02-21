class Node:
    """ Node do grafo de busca """
    
    def __init__(self,pai=None, estado=None, custo=0,
                    acao=None, filhos=[]):
        self.pai = pai
        self.estado = estado
        self.custo= custo
        self.acao = acao
        self.filhos = filhos
    def __str__(self):
        acao = str(self.acao) + ','
        estado = str(self.estado) + ','
        custo =  str(self.custo) + ','
        if self.pai:
            pai =  str(self.pai.estado)
        else :
            pai = "Primeiro Nodo"
            

        return str('(' + acao + estado + custo + pai + ')')
