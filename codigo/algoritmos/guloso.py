class alogiritmo_guloso:

    def maior_valor(self, lances, energia_disponivel):
        """
        Calcula o maior valor possível dentro do limite de energia disponível, selecionando os lances com os maiores valores absolutos.

        Este método ordena os lances em ordem decrescente de valor e, em seguida, seleciona os lances até que o limite de energia disponível seja alcançado ou excedido. O objetivo é maximizar o valor total sem ultrapassar a energia disponível.

        Parâmetros:
        - lances: Uma lista de tuplas, onde cada tupla representa um lance e contém dois elementos: a quantidade de energia (lote) e o valor do lance.
        - energia_disponivel: A quantidade de energia disponível para ser alocada.

        Retorna:
        - O valor total alcançado pela seleção dos lances dentro do limite de energia disponível.
        """

        lances.sort(key=lambda x: x[1], reverse=True)
        total_value, total_energy = 0, 0
        for lote, valor in lances:
            if total_energy + lote <= energia_disponivel:
                total_energy += lote
                total_value += valor

        print(f"Executando guloso com {len(lances)} lances e {energia_disponivel} energia disponível\n")
        for i, lance in enumerate(lances):
            print(f"Lance {i}: {lance[0]}, {lance[1]} dinheiros - Valor Total: {total_value}\n")

        return total_value

    def maior_valor_por_megawatts(self, lances, energia_disponivel):
        """
        Calcula o maior valor possível dentro do limite de energia disponível, selecionando os lances com os maiores valores por unidade de energia.

        Este método ordena os lances em ordem decrescente de valor por unidade de energia (valor/megawatt) e, em seguida, seleciona os lances até que o limite de energia disponível seja alcançado ou excedido. O objetivo é maximizar o valor total sem ultrapassar a energia disponível.

        Parâmetros:
        - lances (list of tuples): Uma lista de tuplas, onde cada tupla representa um lance e contém dois elementos: a quantidade de energia (lote) e o valor do lance.
        - energia_disponivel (int/float): A quantidade de energia disponível para ser alocada.

        Retorna:
        - int/float: O valor total alcançado pela seleção dos lances dentro do limite de energia disponível.
        """

        lances.sort(key=lambda x: x[1] / x[0], reverse=True)
        total_value, total_energy = 0, 0
        for lote, valor in lances:
            if total_energy + lote <= energia_disponivel:
                total_energy += lote
                total_value += valor
        print('\n------------------------------------------------------------------------\n')
        print(f"Executando guloso com com {len(lances)} lances e {energia_disponivel} energia disponível...\n")
        for i, lance in enumerate(lances):
            print(f"Lance {i}: {lance[0]}, {lance[1]} dinheiros - Valor Total: {total_value}\n")

        return total_value
