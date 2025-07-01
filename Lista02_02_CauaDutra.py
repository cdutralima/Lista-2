
"""
 Título:              ---Contador de Elementos Pares em um Vetor---
 Finalidade:  Este programa solicita ao usuário que insira 40 números inteiros,
              armazena esses números em uma lista (vetor) e, ao final,
              conta e exibe a quantidade de números pares presentes na lista.
 Autor:       Cauã Dutra Lima da SIlva
 Data:        22 de junho de 2025
"""

# --- INÍCIO DO PROGRAMA ---

# Imprime um cabeçalho para o usuário saber o que o programa faz.
print("-" * 50)
print("Analisador de Vetor - Contagem de Números Pares")
print("-" * 50)
print("Por favor, insira 40 números inteiros.")

# Inicializa uma lista vazia que funcionará como o nosso vetor.
vetor = []

# Inicializa a variável que contará os números pares.
contador_pares = 0

# Define o número de elementos que o vetor terá.
tamanho_vetor = 40

# Inicia um laço de repetição para ler os 40 números do usuário.
# O laço vai de 1 até 40 para facilitar a mensagem ao usuário.
for i in range(tamanho_vetor):
    while True:
        try:
            # Solicita ao usuário que insira um número.
            entrada = input(f"Digite o {i + 1}º número de {tamanho_vetor}: ")
            # Converte a entrada do usuário para um número inteiro.
            numero = int(entrada)
            # Adiciona o número ao final da lista (vetor).
            vetor.append(numero)
            # Sai do laço 'while' se a conversão for bem-sucedida.
            break
        except ValueError:
            # Informa ao usuário que a entrada é inválida e solicita novamente.
            print("Erro: Por favor, digite um número inteiro válido.")

# --- Processamento dos Dados ---

# Comenta que o próximo bloco fará a verificação dos elementos.
# Percorre cada 'numero' dentro da lista 'vetor' que foi preenchida.
for numero in vetor:
    # Verifica se o resto da divisão do número por 2 é igual a 0.
    # Esta é a condição para um número ser par.
    if numero % 2 == 0:
        # Se o número for par, incrementa o contador.
        contador_pares += 1

# --- Exibição dos Resultados ---

# Imprime uma linha para separar a entrada da saída.
print("\n" + "=" * 50)

# Mostra o vetor completo que foi inserido pelo usuário (opcional, mas bom para conferência).
print(f"O vetor completo inserido foi: {vetor}")

# Exibe o resultado final da contagem de números pares.
print(f"Análise concluída: foram encontrados {contador_pares} elementos pares no vetor.")
print("=" * 50)