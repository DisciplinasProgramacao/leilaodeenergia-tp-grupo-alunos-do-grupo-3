def divisao_conquista(lances, energia_disponivel, memo=None):
    if memo is None:
        memo = {}

    if not lances or energia_disponivel <= 0:
        return 0

    if len(lances) == 1:  # Condição de parada ao ter uma única oferta
        return lances[0][1] if lances[0][0] <= energia_disponivel else 0

    chave = (len(lances), energia_disponivel)
    if chave in memo:
        return memo[chave]

    meio = len(lances) // 2
    esquerda = lances[:meio]
    direita = lances[meio:]

    max_esquerda = divisao_conquista(esquerda, energia_disponivel, memo)
    max_direita = divisao_conquista(direita, energia_disponivel, memo)

    melhor_comb = 0
    for e_lote, e_valor in esquerda:
        if e_lote <= energia_disponivel:
            restante = energia_disponivel - e_lote
            melhor_comb = max(melhor_comb, e_valor + divisao_conquista(direita, restante, memo))

    resultado = max(max_esquerda, max_direita, melhor_comb)
    memo[chave] = resultado

    return resultado