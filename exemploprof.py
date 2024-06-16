# Definição das empresas interessadas
interessadas = [
    {"nome": "I1", "megawatts": 500, "valor": 500},
    {"nome": "I2", "megawatts": 500, "valor": 510},
    {"nome": "I3", "megawatts": 400, "valor": 520},
    {"nome": "I4", "megawatts": 300, "valor": 400},
    {"nome": "I5", "megawatts": 200, "valor": 220},
    {"nome": "I6", "megawatts": 900, "valor": 1110},
]

# Quantidade total de energia disponível para venda
total_energia = 1000

def solucaoAceitavel(energia_restante, valor_atual, combinacao_atual):
    # Neste caso, qualquer solução é aceitável, contanto que a energia restante seja >= 0
    return energia_restante >= 0

def solucaoDefinitiva(energia_restante, valor_atual, combinacao_atual):
    # Consideramos que encontramos uma solução se a energia restante for 0 ou se não há mais candidatos
    return energia_restante == 0

def backtracking(energia_restante, valor_atual, combinacao_atual, melhor_valor, melhor_combinacao):
    if solucaoDefinitiva(energia_restante, valor_atual, combinacao_atual):
        if valor_atual > melhor_valor[0]:
            melhor_valor[0] = valor_atual
            melhor_combinacao[0] = combinacao_atual[:]
        return
    
    for candidato in interessadas:
        if candidato not in combinacao_atual and energia_restante >= candidato["megawatts"]:
            combinacao_atual.append(candidato)
            backtracking(energia_restante - candidato["megawatts"], valor_atual + candidato["valor"], combinacao_atual, melhor_valor, melhor_combinacao)
            combinacao_atual.pop()

def encontra_melhor_venda(total_energia, interessadas):
    melhor_valor = [0]
    melhor_combinacao = [[]]
    backtracking(total_energia, 0, [], melhor_valor, melhor_combinacao)
    return melhor_valor[0], melhor_combinacao[0]

# Execução do algoritmo
melhor_valor, melhor_combinacao = encontra_melhor_venda(total_energia, interessadas)

# Impressão dos resultados
print(f"Melhor valor obtido: {melhor_valor}")
print("Melhor combinação de vendas:")
for empresa in melhor_combinacao:
    print(f"{empresa['nome']}: {empresa['megawatts']} megawatts por {empresa['valor']} dinheiros")
