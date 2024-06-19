def greedy_max_value(lances, energia_disponivel):
    lances.sort(key=lambda x: x[1], reverse=True)
    total_value, total_energy = 0, 0
    for lote, valor in lances:
        if total_energy + lote <= energia_disponivel:
            total_energy += lote
            total_value += valor

    print(f"Executando guloso com {len(lances)} lances e {energia_disponivel} energia disponível")
    for i, lance in enumerate(lances):
        print(f"Lance {i}: {lance[0]}, {lance[1]} reais - Valor Total: {total_value}\n")

    return total_value

def greedy_max_value_per_mw(lances, energia_disponivel):
    lances.sort(key=lambda x: x[1] / x[0], reverse=True)
    total_value, total_energy = 0, 0
    for lote, valor in lances:
        if total_energy + lote <= energia_disponivel:
            total_energy += lote
            total_value += valor

    print(f"Executando guloso com com {len(lances)} lances e {energia_disponivel} energia disponível")
    for i, lance in enumerate(lances):
        print(f"Lance {i}: {lance[0]}, {lance[1]} reais - Valor Total: {total_value}\n")

    return total_value
