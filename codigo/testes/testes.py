import sys
import os
import time

sys.setrecursionlimit(5000)  # Ajuste conforme necessário

# Adicionar o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.gerar_conjuntos import gerar_conjuntos
from algoritmos.backtraking import backtracking
from algoritmos.guloso import greedy_max_value, greedy_max_value_per_mw
from algoritmos.divisão_conquista import divide_and_conquer
from algoritmos.programação_dinamica import dp_solution

def medir_tempo_algoritmos(conjuntos, energia_disponivel):
    resultados_guloso1 = []
    resultados_guloso2 = []
    tempos_guloso1 = []
    tempos_guloso2 = []

    for idx, lances in enumerate(conjuntos):
        print(f"Rodando conjunto {idx + 1} com guloso")
        inicio = time.time()
        resultado1 = greedy_max_value(lances, energia_disponivel)
        fim = time.time()
        tempos_guloso1.append(fim - inicio)
        resultados_guloso1.append(resultado1)

        inicio = time.time()
        resultado2 = greedy_max_value_per_mw(lances, energia_disponivel)
        fim = time.time()
        tempos_guloso2.append(fim - inicio)
        resultados_guloso2.append(resultado2)

    return (resultados_guloso1, tempos_guloso1), (resultados_guloso2, tempos_guloso2)


def medir_tempo_backtracking(conjuntos, energia_disponivel):
    tempos = []
    tamanho_T = 0
    for idx, lances in enumerate(conjuntos):
        print(f"Rodando conjunto {idx + 1} com backtracking")
        inicio = time.time()
        backtracking(lances, energia_disponivel)
        fim = time.time()
        duracao = fim - inicio
        tempos.append(duracao)
        if duracao > 30:
            break
        tamanho_T = len(lances)
    return tamanho_T, tempos


def medir_tempo_dc_pd(conjuntos, energia_disponivel):
    resultados_dc = []
    resultados_pd = []
    tempos_dc = []
    tempos_pd = []

    for idx, lances in enumerate(conjuntos):
        print(f"Rodando conjunto {idx + 1} com divisão e conquista")
        inicio = time.time()
        resultado_dc = divide_and_conquer(lances, energia_disponivel)
        fim = time.time()
        tempos_dc.append(fim - inicio)
        resultados_dc.append(resultado_dc)

        print(f"Rodando conjunto {idx + 1} com programação dinâmica")
        inicio = time.time()
        resultado_pd = dp_solution(lances, energia_disponivel)
        fim = time.time()
        tempos_pd.append(fim - inicio)
        resultados_pd.append(resultado_pd)

    return (resultados_dc, tempos_dc), (resultados_pd, tempos_pd)


def main():
    tam_max = 100  # Pode ser ajustado conforme necessidade
    incremento = 1
    energia_disponivel = 1000

    print("Gerando conjuntos de teste para backtracking...")
    conjuntos_de_teste = gerar_conjuntos(tam_max, incremento)
    tamanho_T, tempos_backtracking = medir_tempo_backtracking(conjuntos_de_teste, energia_disponivel)
    print(f'Tamanho T encontrado para backtracking: {tamanho_T}')
    
    print("Gerando conjuntos de teste adicionais para algoritmos gulosos...")
    tamanho_10T = 10 * tamanho_T
    conjuntos_de_teste_guloso = gerar_conjuntos(tamanho_10T, tamanho_T)
    
    (resultados1, tempos1), (resultados2, tempos2) = medir_tempo_algoritmos(conjuntos_de_teste_guloso, energia_disponivel)
    print(f'Médias dos resultados e tempos do primeiro algoritmo guloso: {sum(resultados1)/len(resultados1)}, {sum(tempos1)/len(tempos1)}')
    print(f'Médias dos resultados e tempos do segundo algoritmo guloso: {sum(resultados2)/len(resultados2)}, {sum(tempos2)/len(tempos2)}')

    (resultados_dc, tempos_dc), (resultados_pd, tempos_pd) = medir_tempo_dc_pd(conjuntos_de_teste_guloso, energia_disponivel)
    print(f'Médias dos resultados e tempos de divisão e conquista: {sum(resultados_dc)/len(resultados_dc)}, {sum(tempos_dc)/len(tempos_dc)}')
    print(f'Médias dos resultados e tempos de programação dinâmica: {sum(resultados_pd)/len(resultados_pd)}, {sum(tempos_pd)/len(tempos_pd)}')

if __name__ == "__main__":
    main()
