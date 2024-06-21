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

def ler_conjunto_empresas(entrada):
    linhas = entrada.strip().split("\n")
    lances = []
    for linha in linhas:
        partes = linha.split(";")
        nome = partes[0]
        quantidade = int(partes[1])
        valor = int(partes[2])
        lances.append((quantidade, valor))
    return lances

conjunto_empresas_1 = """
E1;430;1043
E2;428;1188
E3;410;1565
E4;385;1333
E5;399;1214
E6;382;1498
E7;416;1540
E8;436;1172
E9;416;1386
E10;423;1097
E11;400;1463
E12;406;1353
E13;403;1568
E14;390;1228
E15;387;1542
E16;390;1206
E17;430;1175
E18;397;1492
E19;392;1293
E20;393;1533
E21;439;1149
E22;403;1277
E23;415;1624
E24;387;1280
E25;417;1330
"""

conjunto_empresas_2 = """
E1;430;1043
E2;428;1188
E3;410;1565
E4;385;1333
E5;399;1214
E6;382;1498
E7;416;1540
E8;436;1172
E9;416;1386
E10;423;1097
E11;400;1463
E12;406;1353
E13;403;1568
E14;390;1228
E15;387;1542
E16;390;1206
E17;430;1175
E18;397;1492
E19;392;1293
E20;393;1533
E21;439;1149
E22;403;1277
E23;415;1624
E24;387;1280
E25;417;1330
E1;313;1496
E2;398;1768
E3;240;1210
E4;433;2327
E5;301;1263
E6;297;1499
E7;232;1209
E8;614;2342
E9;558;2983
E10;495;2259
E11;310;1381
E12;213;961
E13;213;1115
E14;346;1552
E15;385;2023
E16;240;1234
E17;483;2828
E18;487;2617
E19;709;2328
E20;358;1847
E21;467;2038
E22;363;2007
E23;279;1311
E24;589;3164
E25;476;2480
"""

energia_disponivel = 8000

def medir_tempo_algoritmos(conjuntos, energia_disponivel):
    resultados_guloso1 = []
    resultados_guloso2 = []
    tempos_guloso1 = []
    tempos_guloso2 = []

    for idx, lances in enumerate(conjuntos):
        print(f"Rodando conjunto {idx + 1} com greedy algorithms")
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

    for idx, lances in conjuntos:
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
    # Ler os conjuntos fornecidos
    conjunto_1 = ler_conjunto_empresas(conjunto_empresas_1)
    conjunto_2 = ler_conjunto_empresas(conjunto_empresas_2)

    # Executar testes para o primeiro conjunto
    print("\nExecutando testes para o conjunto de empresas interessadas 1\n")
    conjuntos_de_teste = [conjunto_1]
    medir_tempo_backtracking(conjuntos_de_teste, energia_disponivel)
    
    (resultados1, tempos1), (resultados2, tempos2) = medir_tempo_algoritmos(conjuntos_de_teste, energia_disponivel)
    print(f'Médias dos resultados e tempos do primeiro algoritmo guloso: {sum(resultados1)/len(resultados1)}, {sum(tempos1)/len(tempos1)}')
    print(f'Médias dos resultados e tempos do segundo algoritmo guloso: {sum(resultados2)/len(resultados2)}, {sum(tempos2)/len(tempos2)}')

    imprimir = medir_tempo_dc_pd(conjuntos_de_teste, energia_disponivel)
    print(f'Médias dos resultados e tempos de divisão e conquista: {sum(imprimir[0][0])/len(imprimir[0][0])}, {sum(imprimir[0][1])/len(imprimir[0][1])}')
    print(f'Médias dos resultados e tempos de programação dinâmica: {sum(imprimir[1][0])/len(imprimir[1][0])}, {sum(imprimir[1][1])/len(imprimir[1][1])}')

    # Executar testes para o segundo conjunto
    print("\nExecutando testes para o conjunto de empresas interessadas 2\n")
    conjuntos_de_teste = [conjunto_2]
    medir_tempo_backtracking(conjuntos_de_teste, energia_disponivel)
    
    (resultados1, tempos1), (resultados2, tempos2) = medir_tempo_algoritmos(conjuntos_de_teste, energia_disponivel)
    print(f'Médias dos resultados e tempos do primeiro algoritmo guloso: {sum(resultados1)/len(resultados1)}, {sum(tempos1)/len(tempos1)}')
    print(f'Médias dos resultados e tempos do segundo algoritmo guloso: {sum(resultados2)/len(resultados2)}, {sum(tempos2)/len(tempos2)}')

    imprimir = medir_tempo_dc_pd(conjuntos_de_teste, energia_disponivel)
    print(f'Médias dos resultados e tempos de divisão e conquista: {sum(imprimir[0][0])/len(imprimir[0][0])}, {sum(imprimir[0][1])/len(imprimir[0][1])}')
    print(f'Médias dos resultados e tempos de programação dinâmica: {sum(imprimir[1][0])/len(imprimir[1][0])}, {sum(imprimir[1][1])/len(imprimir[1][1])}')


if __name__ == "__main__":
    main()
