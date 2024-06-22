import sys
import os
import time

sys.setrecursionlimit(5000)  # Ajuste conforme necessário

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

def medir_tempo_algoritmos(lances, energia_disponivel):
    inicio = time.time()
    resultado_guloso1 = greedy_max_value(lances, energia_disponivel)
    fim = time.time()
    tempo_guloso1 = fim - inicio

    inicio = time.time()
    resultado_guloso2 = greedy_max_value_per_mw(lances, energia_disponivel)
    fim = time.time()
    tempo_guloso2 = fim - inicio

    return (resultado_guloso1, tempo_guloso1), (resultado_guloso2, tempo_guloso2)


def medir_tempo_backtracking(lances, energia_disponivel):
    inicio = time.time()
    resultado = backtracking(lances, energia_disponivel)
    fim = time.time()
    return resultado, fim - inicio


def medir_tempo_dc_pd(lances, energia_disponivel):
    inicio = time.time()
    resultado_dc = divide_and_conquer(lances, energia_disponivel)
    fim = time.time()
    tempo_dc = fim - inicio

    inicio = time.time()
    resultado_pd = dp_solution(lances, energia_disponivel)
    fim = time.time()
    tempo_pd = fim - inicio

    return (resultado_dc, tempo_dc), (resultado_pd, tempo_pd)


def main():
    # Ler os conjuntos fornecidos
    conjunto_1 = ler_conjunto_empresas(conjunto_empresas_1)
    conjunto_2 = ler_conjunto_empresas(conjunto_empresas_2)

    for idx, conjunto in enumerate([conjunto_1, conjunto_2], start=1):
        print(f"\nExecutando testes para o conjunto de empresas interessadas {idx}\n")

        # Backtracking
        resultado_backtracking, tempo_backtracking = medir_tempo_backtracking(conjunto, energia_disponivel)
        print(f"Backtracking -> Resultado: {resultado_backtracking}, Tempo: {tempo_backtracking:.2f}s")

        # Algoritmos Gulosos
        (resultado_guloso1, tempo_guloso1), (resultado_guloso2, tempo_guloso2) = medir_tempo_algoritmos(conjunto, energia_disponivel)
        print(f"Guloso (Maior Valor) -> Resultado: {resultado_guloso1}, Tempo: {tempo_guloso1:.2f}s")
        print(f"Guloso (Maior Valor por MW) -> Resultado: {resultado_guloso2}, Tempo: {tempo_guloso2:.2f}s")

        # Divisão e Conquista e Programação Dinamica
        (resultado_dc, tempo_dc), (resultado_pd, tempo_pd) = medir_tempo_dc_pd(conjunto, energia_disponivel)
        print(f"Divisão e Conquista -> Resultado: {resultado_dc}, Tempo: {tempo_dc:.2f}s")
        print(f"Programação Dinâmica -> Resultado: {resultado_pd}, Tempo: {tempo_pd:.2f}s")

    # Adicionando a mensagem de conclusão dos testes
    print("\nTodos os testes foram concluídos com sucesso!\n")


if __name__ == "__main__":
    main()
