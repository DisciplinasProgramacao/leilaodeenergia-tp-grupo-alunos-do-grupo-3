def backtracking(lances, energia_disponivel):
    def solver(posicao, energia_restante):
        if posicao >= len(lances):
            return 0
        if energia_restante <= 0:
            return 0

        lance = lances[posicao]
        if lance[0] > energia_restante:
            return solver(posicao + 1, energia_restante)  # Pular lances B se não couber

        incluir = lance[1] + solver(posicao + 1, energia_restante - lance[0])
        nao_incluir = solver(posicao + 1, energia_restante)

        return max(incluir, nao_incluir)

    print(f"Executando backtracking com {len(lances)} lances e {energia_disponivel} energia disponível")
    for i, lance in enumerate(lances):
        print(f"Lance {i}: {lance[0]}, {lance[1]} reais")

    resultado = solver(0, energia_disponivel)
    print(f"Valor máximo obtido por backtracking: {resultado}\n")
    return resultado
