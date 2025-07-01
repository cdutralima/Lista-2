"""
-------------------------------------------------------------------------------
 Título:                  ---Ordenação de Vetor---
 Finalidade:  Este programa gera um vetor (lista) com 100 elementos
              numéricos aleatórios e depois o ordena em ordem crescente
              utilizando o algoritmo de ordenação Bubble Sort, sem usar
              qualquer método ou função de ordenação nativa do Python.
 Autor:       Cauã Dutra Lima da Silva
 Data:        24 de junho de 2025
"""

# Importa o módulo 'random' para gerar os números aleatórios.
import random

# --- 1. Geração do Vetor Aleatório ---

# Define as constantes para a criação do vetor.
TAMANHO_VETOR = 100
VALOR_MINIMO = 1
VALOR_MAXIMO = 1000

# Cria o vetor com 100 elementos inteiros aleatórios.
vetor_original = [random.randint(VALOR_MINIMO, VALOR_MAXIMO) for _ in range(TAMANHO_VETOR)]

print("=" * 60)
print("          Ordenação de Vetor com Bubble Sort")
print("=" * 60)

# Imprime o vetor original, antes da ordenação.
print("\n--- Vetor Original (Desordenado) ---")
print(vetor_original)

# --- 2. Ordenação com o Algoritmo Bubble Sort ---

# É uma boa prática criar uma cópia do vetor para não modificar o original.
vetor_ordenado = vetor_original.copy()

# Pega o tamanho do vetor para usar nos laços.
n = len(vetor_ordenado)

# Inicia o algoritmo Bubble Sort.
# O primeiro laço (externo) percorre o vetor para garantir que cada
# elemento seja comparado. Ele precisa rodar n-1 vezes.
for i in range(n - 1):
    # O segundo laço (interno) é onde as comparações e trocas acontecem.
    # Ele "borbulha" o maior elemento da passagem atual para o final da
    # parte não ordenada do vetor.
    # A cada passagem 'i', o i-ésimo maior elemento já está no lugar certo,
    # por isso o laço interno vai até 'n-i-1'.
    for j in range(0, n - i - 1):
        # Compara o elemento atual com o próximo.
        if vetor_ordenado[j] > vetor_ordenado[j + 1]:
            # Se o elemento atual for maior, troca eles de lugar.
            # Esta é uma forma "pythônica" de fazer a troca sem uma variável temporária.
            vetor_ordenado[j], vetor_ordenado[j + 1] = vetor_ordenado[j + 1], vetor_ordenado[j]

# --- 3. Exibição do Resultado ---

# Imprime o vetor final, agora ordenado.
print("\n--- Vetor Final (Ordenado com Bubble Sort) ---")
print(vetor_ordenado)
print("\n" + "=" * 60)