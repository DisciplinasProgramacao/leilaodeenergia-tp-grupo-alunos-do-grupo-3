import sys
import os
import time
import threading
sys.setrecursionlimit(5000)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from data.gerar_conjuntos import gerar_conjuntos
from algoritmos.backtracking import algoritmo_backtracking
from algoritmos.guloso import alogiritmo_guloso
from algoritmos.divisão_conquista import algoritmo_divisao_conquista
from algoritmos.programação_dinamica import algoritmo_programacao_dinamica
import csv

# Variavel Global
energia_disponivel = 8000

def ler_conjunto_empresas(path):
    """
    Método para ler um arquivo CSV contendo os lances das empresas e os converte em uma lista de tuplas.

    Cada linha do arquivo CSV deve conter o nome da empresa, a quantidade de energia (em megawatts) que a empresa deseja vender e o valor (em reais) pelo qual deseja vender essa quantidade de energia. As colunas devem ser separadas por vírgulas.

    Parâmetros:
    - path: O caminho do arquivo CSV a ser lido.

    Retorna:
    - Uma lista de tuplas, onde cada tupla contém dois inteiros: a quantidade de energia (em megawatts) e o valor (em reais) de cada lance.
    """

    conjunto_empresas = ""
    with open(path, newline='') as arquivo_csv:
        leitor = csv.reader(arquivo_csv, delimiter=',')
        next(leitor) 
        for row in leitor:
            conjunto_empresas += ';'.join(row) + '\n'

    linhas = conjunto_empresas.strip().split("\n")
    lances = []
    for linha in linhas:
        partes = linha.split(";")
        nome = partes[0]
        quantidade = int(partes[1])
        valor = int(partes[2])
        lances.append((quantidade, valor))
    return lances

def medir_tempo_algoritmos(lances, energia_disponivel):
    """
    Mede o tempo de execução dos dois algoritmos guloso, um sendo considerado o maior valor dos lances
    e outro considerando o maior valor por megawatt, os lances e a energia disponível.

    Args:
    - lances: Uma lista de tuplas, onde cada tupla representa um lance no formato (identificador, megawatts, valor).
    - energia_disponivel: A quantidade de energia disponível para ser alocada.

    Returns:
    - Retorna um par de tuplas, onde cada tupla contém o resultado do algoritmo e o tempo de execução correspondente.
    """

    guloso = alogiritmo_guloso()

    inicio = time.time()
    resultado_guloso1 = guloso.maior_valor(lances, energia_disponivel)
    fim = time.time()
    tempo_guloso1 = fim - inicio

    inicio = time.time()
    resultado_guloso2 = guloso.maior_valor_por_megawatts(lances, energia_disponivel)
    fim = time.time()
    tempo_guloso2 = fim - inicio

    return (resultado_guloso1, tempo_guloso1), (resultado_guloso2, tempo_guloso2)

def medir_tempo_backtracking(lances, energia_disponivel, timeout=30):
    """
    Mede o tempo de execução do backtracking, lances, a energia disponível e o tempo limite para a execução.

    Args:
    - lances: Uma lista de tuplas, onde cada tupla representa um lance no formato (identificador, megawatts, valor).
    - energia_disponivel: A quantidade de energia disponível para ser alocada.
    - timeout: O tempo limite em segundos para a execução do algoritmo. Padrão é 30 segundos.

    Returns:
    - Retorna o melhor resultado encontrado pelo algoritmo de backtracking dentro do tempo limite.
    """

    bt = algoritmo_backtracking()

    melhor_resultado = [0] 
    
    def worker():
        nonlocal melhor_resultado
        resultado = bt.backtracking(lances, energia_disponivel)
        melhor_resultado[0] = resultado if resultado is not None else 0
    
    thread = threading.Thread(target=worker)
    thread.start()
    thread.join(timeout)
    
    if thread.is_alive():
        print("Backtracking interrompido após tempo limite!")
        thread.join()
    
    return melhor_resultado[0]

def medir_tempo_dc_pd(lances, energia_disponivel):

    """
    Mede e compara o tempo de execução dos algoritmos de divisão e conquista (DC) e programação dinâmica (PD).

    Este método executa ambos os algoritmos, DC e PD, usando o mesmo conjunto de dados de entrada e a mesma quantidade de energia disponível. Ele mede o tempo de execução de cada algoritmo e retorna os tempos medidos, permitindo uma comparação direta entre a eficiência dos dois métodos.

    Parâmetros:
    - conjunto: Uma lista de objetos ou valores que serão processados pelos algoritmos. Cada elemento do conjunto representa um dado de entrada para os algoritmos.
    - energia_disponivel: A quantidade de energia disponível para os algoritmos processarem o conjunto. Este valor é utilizado como um limite nos cálculos realizados pelos algoritmos.

    Retorna:
    - tUma tupla contendo dois elementos. O primeiro elemento é o tempo de execução do algoritmo de divisão e conquista, e o segundo elemento é o tempo de execução do algoritmo de programação dinâmica.
    """

    dc = algoritmo_divisao_conquista()
    pd = algoritmo_programacao_dinamica()

    inicio = time.time()
    resultado_dc = dc.divisao_conquista(lances, energia_disponivel)
    fim = time.time()
    tempo_dc = fim - inicio

    inicio = time.time()
    resultado_pd = pd.prog_dinamica(lances, energia_disponivel)
    fim = time.time()
    tempo_pd = fim - inicio

    return (resultado_dc, tempo_dc), (resultado_pd, tempo_pd)

def main():

    conjunto_empresas_1 = ler_conjunto_empresas('conjunto_empresas_1.csv')
    conjunto_empresas_2 = ler_conjunto_empresas('conjunto_empresas_2.csv')
    conjunto_empresas_aleatorias_1 = ler_conjunto_empresas('conjunto_empresas_aleatorias_1.csv')
    conjunto_empresas_aleatorias_2 = ler_conjunto_empresas('conjunto_empresas_aleatorias_2.csv')
    conjunto_empresas_aleatorias_3 = ler_conjunto_empresas('conjunto_empresas_aleatorias_3.csv')
    conjunto_empresas_aleatorias_4 = ler_conjunto_empresas('conjunto_empresas_aleatorias_4.csv')


    resultados = {}

    for idx, conjunto in enumerate([conjunto_empresas_1, conjunto_empresas_2, conjunto_empresas_aleatorias_1, conjunto_empresas_aleatorias_2, conjunto_empresas_aleatorias_3, conjunto_empresas_aleatorias_4], start=1):
        conjunto_nome = f"Conjunto {idx}"
        resultados[conjunto_nome] = {}

        print(f"\nExecutando testes para o {conjunto_nome}\n")

        print('\n************************************************************************\n')

        # Gulosos
        (resultado_guloso1, tempo_guloso1), (resultado_guloso2, tempo_guloso2) = medir_tempo_algoritmos(conjunto, energia_disponivel)
        resultados[conjunto_nome]['Guloso (Maior Valor)'] = (resultado_guloso1, tempo_guloso1)
        resultados[conjunto_nome]['Guloso (Maior Valor por MW)'] = (resultado_guloso2, tempo_guloso2)
        print(f"Guloso (Maior Valor) -> Resultado: {resultado_guloso1}, Tempo: {tempo_guloso1:.2f}s")
        print(f"Guloso (Maior Valor por MW) -> Resultado: {resultado_guloso2}, Tempo: {tempo_guloso2:.2f}s")

        print('\n************************************************************************\n')

        # Programação Dinâmica e Divisão e Conquista
        (resultado_dc, tempo_dc), (resultado_pd, tempo_pd) = medir_tempo_dc_pd(conjunto, energia_disponivel)
        resultados[conjunto_nome]['Divisão e Conquista'] = (resultado_dc, tempo_dc)
        resultados[conjunto_nome]['Programação Dinâmica'] = (resultado_pd, tempo_pd)
        print(f"Divisão e Conquista -> Resultado: {resultado_dc}, Tempo: {tempo_dc:.2f}s")
        print(f"Programação Dinâmica -> Resultado: {resultado_pd}, Tempo: {tempo_pd:.2f}s")

        print('\n************************************************************************\n')

        # Backtracking
        inicio = time.time()
        resultado_backtracking = medir_tempo_backtracking(conjunto, energia_disponivel)
        fim = time.time()
        tempo_backtracking = fim - inicio
        resultados[conjunto_nome]['Backtracking'] = (resultado_backtracking, tempo_backtracking)
        print(f"Backtracking -> Resultado: {resultado_backtracking}, Tempo: {tempo_backtracking:.2f}s")

    print("\nTodos os testes foram concluídos com sucesso!\n")

    print("\nResumo dos Resultados:\n")
    for conjunto, res in resultados.items():
        print(f"{conjunto}:")
        for algoritmo, (resultado, tempo) in res.items():
            print(f"  {algoritmo} => Resultado: {resultado}, Tempo: {tempo:.2f}s")
        print("\n")

if __name__ == "__main__":
    main()
