def divide_and_conquer(lances, energia_disponivel):
    if not lances or energia_disponivel <= 0:
        return 0
    
    if len(lances) == 1:  # Condição de parada ao ter uma única oferta
        return lances[0][1] if lances[0][0] <= energia_disponivel else 0

    meio = len(lances) // 2
    esquerda = lances[:meio]
    direita = lances[meio:]

    print(f"Executando divisão e conquista com {len(lances)} lances e {energia_disponivel} energia disponível")
    
    max_esquerda = divide_and_conquer(esquerda, energia_disponivel)
    max_direita = divide_and_conquer(direita, energia_disponivel)

    melhor_comb = 0
    for e_lote, e_valor in esquerda:
        if e_lote <= energia_disponivel:
            restante = energia_disponivel - e_lote
            melhor_comb = max(melhor_comb, e_valor + divide_and_conquer(direita, restante))

    resultado = max(max_esquerda, max_direita, melhor_comb)
    print(f"Divisão e Conquista - Valor Total: {resultado}\n")

    return resultado
