"""
-------------------------------------------------------------------------------
 Título:             ---Cálculo de Pi por Série Numérica---
 Finalidade:  Este programa calcula uma aproximação do valor de Pi (π)
              usando a soma dos 'n' primeiros termos da série de Madhava,
              conforme a fórmula fornecida. O programa solicita ao usuário
              que insira o número de termos (n) a serem usados.
 Autor:       Cauã Dutra Lima da Silva
 Data:        24 de junho de 2025
"""

# Importa o módulo 'math' para usar a função de raiz quadrada (sqrt)
# e o valor de 'pi' para comparação.
import math

# --- INÍCIO DO PROGRAMA ---

# Imprime um cabeçalho para o usuário.
print("-" * 60)
print("     Cálculo do Valor de π (Pi) por Soma de Série")
print("-" * 60)

# --- Leitura do Número de Termos (n) ---

# Solicita ao usuário o número de termos para a série.
while True:
    try:
        # Pede ao usuário para digitar o número de termos.
        n = int(input("Digite o número de termos (n) para calcular a série: "))
        # Verifica se n é um número positivo.
        if n > 0:
            break
        else:
            print("Erro: O número de termos deve ser um inteiro positivo.")
    except ValueError:
        # Garante que o usuário digitou um número inteiro.
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# --- Cálculo da Série ---

# Inicializa a variável que vai armazenar a soma da série interna.
soma_serie = 0.0

# Inicia um laço que vai de 1 até n (inclusive).
for k in range(1, n + 1):
    # Calcula o k-ésimo termo da série: (-1)^(k+1) / k^2
    # Ex: k=1 -> 1/1, k=2 -> -1/4, k=3 -> 1/9
    termo = ((-1)**(k + 1)) / (k**2)
    # Adiciona o termo calculado à soma total.
    soma_serie += termo

# Aplica a fórmula final para encontrar a aproximação de pi.
# pi ≈ sqrt(12 * soma_serie)
pi_aproximado = math.sqrt(12 * soma_serie)

# --- Exibição do Resultado ---

print("\n" + "=" * 60)
print("R E S U L T A D O")
print("=" * 60)
print(f"Número de termos utilizados (n): {n}")
print(f"O valor de π aproximado pela série é: {pi_aproximado}")
print(f"Valor de π (referência da biblioteca math): {math.pi}")
print("=" * 60)
print("\nNota: Quanto maior o número de termos (n), mais precisa será a aproximação.")
