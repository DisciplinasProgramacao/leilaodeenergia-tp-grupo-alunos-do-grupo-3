import time

class algoritmo_backtracking:

    def backtracking(self, lances, energia_disponivel):
        
        """
        Resolve o problema de alocação de recursos usando o algoritmo de backtracking.

        Este método tenta encontrar a melhor maneira de alocar uma quantidade limitada de recursos (energia_disponivel) entre várias opções (lances), de modo a maximizar o valor total obtido. Cada lance é representado por uma tupla contendo a quantidade de recursos (mw) e o valor associado (dinheiros).

        O algoritmo explora todas as combinações possíveis de lances, incluindo ou excluindo cada um deles, para encontrar a combinação que maximiza o valor total sem exceder a quantidade de recursos disponíveis. Para evitar que a execução se prolongue indefinidamente, há um limite de tempo de 30 segundos para a busca.

        Parâmetros:
        - lances: Uma lista de tuplas, onde cada tupla representa um lance e contém dois elementos: a quantidade de recursos (mw) e o valor do lance (dinheiros).
        - energia_disponivel: A quantidade total de recursos disponíveis para alocação.

        Retorna:
        - O valor total máximo que pode ser obtido com a alocação ótima dos recursos disponíveis.

       """

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

        print(f"Executando backtracking com {len(lances)} lances e {energia_disponivel} energia disponível\n")
        for i, lance in enumerate(lances):
            print(f"Lance {i}: {lance[0]}, {lance[1]} dinheiros\n")

        valor_maximo = resultado(0, energia_disponivel)
        print(f"Valor máximo obtido por backtracking: {valor_maximo}\n")
        return valor_maximo

