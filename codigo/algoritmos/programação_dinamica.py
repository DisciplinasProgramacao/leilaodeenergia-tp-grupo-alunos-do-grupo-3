class algoritmo_programacao_dinamica:

    def prog_dinamica(self, lances, energia_disponivel):

        """
        Calcula o valor máximo que pode ser obtido com uma lista de lances dentro de um limite de energia disponível.

        Utiliza uma abordagem de divisão e conquista, dividindo a lista de lances em duas metades, resolvendo cada metade de forma independente e, em seguida, encontrando a melhor combinação entre as soluções das metades. Utiliza memoização para otimizar a execução, evitando o recálculo de subproblemas já resolvidos.

        Parâmetros:
        - lances: Uma lista de tuplas, onde cada tupla representa um lance e contém dois elementos: a quantidade de energia (em megawatts) e o valor do lance (em unidades monetárias).
        - energia_disponivel: A quantidade de energia disponível para ser alocada (em megawatts).
        - memo: Um dicionário usado para armazenar os resultados de subproblemas já calculados. Padrão é None, o que significa que nenhum resultado de subproblema é inicialmente armazenado.

        Retorna:
        - O valor máximo que pode ser obtido dada a lista de lances e o limite de energia disponível.
        """

        dp = [0] * (energia_disponivel + 1)
        for mw, valor in lances:
            for i in range(energia_disponivel, mw - 1, -1):
                dp[i] = max(dp[i], dp[i - mw] + valor)

        print(f"Executando programação dinamica com {len(lances)} lances e {energia_disponivel} energia disponível\n")
        for i, lance in enumerate(lances):
            print(f"Lance {i}: {lance[0]}, {lance[1]} dinheiros\n")

        resultado = dp[energia_disponivel]
        print(f"Programação Dinâmica - Valor Total: {resultado}\n")

        return resultado
