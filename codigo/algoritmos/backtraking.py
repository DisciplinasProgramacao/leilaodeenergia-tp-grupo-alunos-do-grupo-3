import time

def backtracking(lances, energia_disponivel):
    start_time = time.time()

    def resultado(posicao, energia_restante):
        if time.time() - start_time > 30:
            return 0
        if posicao >= len(lances):
            return 0
        if energia_restante <= 0:
            return 0

        lance = lances[posicao]
        if lance[0] > energia_restante:
            return resultado(posicao + 1, energia_restante)

        incluir = lance[1] + resultado(posicao + 1, energia_restante - lance[0])
        nao_incluir = resultado(posicao + 1, energia_restante)

        return max(incluir, nao_incluir)

    print(f"Executando backtracking com {len(lances)} lances e {energia_disponivel} energia disponível")
    for i, lance in enumerate(lances):
        print(f"Lance {i}: {lance[0]}, {lance[1]} dinheiros")

    valor_maximo = resultado(0, energia_disponivel)
    print(f"Valor máximo obtido por backtracking: {valor_maximo}\n")
    return valor_maximo

