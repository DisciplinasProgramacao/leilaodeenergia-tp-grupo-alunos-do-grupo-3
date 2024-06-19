def dp_solution(lances, energia_disponivel):
    dp = [0] * (energia_disponivel + 1)
    for mw, valor in lances:
        for i in range(energia_disponivel, mw - 1, -1):
            dp[i] = max(dp[i], dp[i - mw] + valor)
    
    print(f"Executando programação dinamica com {len(lances)} lances e {energia_disponivel} energia disponível")
    for i, lance in enumerate(lances):
        print(f"Lance {i}: {lance[0]}, {lance[1]} reais")

    resultado = dp[energia_disponivel]
    print(f"Programação Dinâmica - Valor Total: {resultado}\n")

    return resultado
