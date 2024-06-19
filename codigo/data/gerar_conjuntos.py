import random

def gerar_conjuntos(tamanho_max, incremento):
    conjuntos = []
    for t in range(10, tamanho_max + 1, incremento):
        lances = []
        for i in range(t):
            energia = random.randint(1, 1000)  # Energias variando entre 1 e 1000 megawatts
            valor = random.randint(1, 2000)  # Valores variando entre 1 e 2000 dinheiros
            lances.append((energia, valor))
        conjuntos.append(lances)
    return conjuntos

