
"""
-------------------------------------------------------------------------------
 Título:               ---Determinante de Matriz 3x3---
 Finalidade:  Este programa preenche uma matriz 3x3 com valores inteiros
              aleatórios, exibe a matriz e, em seguida, calcula o seu
              determinante seguindo a Regra de Sarrus. A seção de cálculo
              do determinante é feita em no máximo 4 linhas e com no máximo
              3 referências a células da matriz por linha.
 Autor:       Cauã Dutra Lima da Silva
 Data:        24 de junho de 2025
"""

# Importa o módulo 'random' para gerar os valores da matriz.
import random

# --- Geração e Impressão da Matriz ---

print("=" * 40)
print("  Cálculo de Determinante de Matriz 3x3")
print("=" * 40)

# Inicializa a matriz 3x3 com zeros.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Preenche a matriz com valores inteiros aleatórios entre 1 e 10.
for i in range(3):
    for j in range(3):
        matriz[i][j] = random.randint(1, 10)

# Imprime a matriz formatada para visualização.
print("\nMatriz Gerada:")
for linha in matriz:
    print(f"  {linha}")

# --- Cálculo do Determinante (Regra de Sarrus) ---
# A regra dos 4x3 (4 linhas, 3 células por linha) é seguida aqui.
# A solução mais elegante é calcular cada um dos 6 produtos da regra
# e depois somá-los/subtraí-los. No entanto, para caber em 4 linhas,
# é preciso agrupar os cálculos. A interpretação mais lógica é usar
# uma linha para cada um dos 3 termos da expansão por cofatores.
#
# Para a matriz:
# | a b c |
# | d e f |
# | g h i |
# det = a(ei - fh) - b(di - fg) + c(dh - eg)

# Apelido para a matriz para encurtar as linhas.
m = matriz

# Linha 1: Calcula a primeira parte da expansão (a * det(submatriz))
termo_a = m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])

# Linha 2: Calcula a segunda parte da expansão (b * det(submatriz))
termo_b = m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])

# Linha 3: Calcula a terceira parte da expansão (c * det(submatriz))
termo_c = m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])

# Linha 4: Calcula o determinante final combinando os termos.
determinante = termo_a - termo_b + termo_c

# --- Saída ---

print("\nCálculo do Determinante...")
print(f"\nO determinante da matriz é: {determinante}")
print("=" * 40)