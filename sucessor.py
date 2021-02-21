#|1|2|3|
#|4|5|6|
#|7|*|8|
def mexe(estado, cursor, direcao):
    """Mexe as pecas do jogo na direcao dada"""
    estado = list(estado)
    if direcao == "direita":
        estado[cursor], estado[cursor + 1] = estado[cursor + 1], estado[cursor]
    if direcao == "esquerda":
        estado[cursor], estado[cursor - 1] = estado[cursor - 1], estado[cursor]
    if direcao == "abaixo":
        estado[cursor], estado[cursor + 3] = estado[cursor + 3], estado[cursor]
    if direcao == "acima":
        estado[cursor], estado[cursor - 3] = estado[cursor - 3], estado[cursor]

    return (direcao, ''.join(estado))

def sucessor(estado):
    """ Retorna os proximos estados do jogo """
    novos_estados = [] 
    cursor = estado.find('_')

    if cursor % 3 != 0: 
        novos_estados.append(mexe(estado, cursor, "esquerda"))
    if cursor % 3 != 2:
        novos_estados.append(mexe(estado, cursor, "direita"))
    if cursor > 2:
        novos_estados.append(mexe(estado, cursor, "acima"))
    if cursor < 6:
        novos_estados.append(mexe(estado, cursor, "abaixo"))
    return novos_estados
