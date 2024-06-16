import time
import random

def solucaoAceitavel(energia_restante, valor_atual, combinacao_atual):
    return energia_restante >= 0

def solucaoDefinitiva(energia_restante, valor_atual, combinacao_atual):
    return energia_restante == 0

def backtracking(energia_restante, valor_atual, combinacao_atual, melhor_valor, melhor_combinacao, interessadas):
    if solucaoDefinitiva(energia_restante, valor_atual, combinacao_atual):
        if valor_atual > melhor_valor[0]:
            melhor_valor[0] = valor_atual
            melhor_combinacao[0] = combinacao_atual[:]
        return
    
    for candidato in interessadas:
        if candidato not in combinacao_atual and energia_restante >= candidato["megawatts"]:
            combinacao_atual.append(candidato)
            backtracking(energia_restante - candidato["megawatts"], valor_atual + candidato["valor"], combinacao_atual, melhor_valor, melhor_combinacao, interessadas)
            combinacao_atual.pop()

def encontra_melhor_venda(total_energia, interessadas):
    melhor_valor = [0]
    melhor_combinacao = [[]]
    backtracking(total_energia, 0, [], melhor_valor, melhor_combinacao, interessadas)
    return melhor_valor[0], melhor_combinacao[0]

def gerar_interessadas(n):
    return [
        {
            "nome": f"I{i}",
            "megawatts": random.randint(50, 1000),
            "valor": random.randint(100, 2000)
        }
        for i in range(1, n + 1)
    ]

def teste_tamanho(tamanho):
    total_energia = 1000
    tempos = []
    for _ in range(10):
        interessadas = gerar_interessadas(tamanho)
        inicio = time.time()
        encontra_melhor_venda(total_energia, interessadas)
        fim = time.time()
        tempos.append(fim - inicio)
    return sum(tempos) / len(tempos)

def main():
    tamanho = 10
    while True:
        tempo_medio = teste_tamanho(tamanho)
        print(f"Tamanho: {tamanho}, Tempo médio: {tempo_medio:.2f} segundos")
        if tempo_medio > 30:
            print(f"Tempo limite de 30 segundos excedido no tamanho {tamanho}")
            break
        tamanho += 1

if __name__ == "__main__":
    main()
