"""
-------------------------------------------------------------------------------
 Título:              ---Troca de Metades de um Vetor---
 Finalidade:  Este programa cria um vetor de 16 posições, divide-o ao meio
              e troca a primeira metade (as 8 primeiras posições) pela
              segunda metade (as 8 últimas posições). Ao final, imprime
              tanto o vetor original quanto o vetor com as posições trocadas.
 Autor:       Cauã Dutra Lima da Silva
 Data:        24 de junho de 2025

"""

# --- INÍCIO DO PROGRAMA ---

# Imprime um cabeçalho para o usuário.
print("-" * 50)
print("Troca de Posições em um Vetor de 16 Elementos")
print("-" * 50)
print("Por favor, insira 16 números inteiros.")

# --- Leitura do Vetor (Input do Usuário) ---

# Inicializa uma lista vazia que funcionará como o nosso vetor.
vetor_original = []
# Define a quantidade de elementos a serem lidos.
tamanho_vetor = 16

# Cria um laço para ler os 16 números do usuário.
for i in range(tamanho_vetor):
    # Usa um laço infinito para garantir que o usuário digite um número válido.
    while True:
        try:
            # Solicita a entrada do número.
            entrada = input(f"Digite o {i + 1}º número de {tamanho_vetor}: ")
            # Tenta converter a entrada para inteiro.
            numero = int(entrada)
            # Adiciona o número ao vetor.
            vetor_original.append(numero)
            # Se a conversão for bem-sucedida, sai do laço 'while' e pede o próximo.
            break
        except ValueError:
            # Caso o usuário não digite um número, exibe uma mensagem de erro.
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# --- Exibição e Processamento ---

print("\n" + "=" * 50)
# Imprime o vetor antes de qualquer modificação.
print("1. Vetor Original Digitado:")
print(vetor_original)

# Pega a segunda metade do vetor (as 8 últimas posições, do índice 8 ao final).
segunda_metade = vetor_original[8:]

# Pega a primeira metade do vetor (as 8 primeiras posições, do início ao índice 7).
primeira_metade = vetor_original[:8]

# Cria o novo vetor combinando as duas metades na ordem inversa.
vetor_trocado = segunda_metade + primeira_metade

# Imprime o vetor após a troca das metades.
print("\n2. Vetor com as metades trocadas:")
print(vetor_trocado)
print("=" * 50)