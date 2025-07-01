"""
 Título:                  ---Analisador de Frases---
 Finalidade:  Este programa lê uma frase fornecida pelo usuário e calcula o
              número total de vogais, o total de espaços em branco e o
              total dos caracteres restantes (consoantes, números, símbolos).
 Autor:       Cauã Dutra Lima da Silva
 Data:        22 de junho de 2025
"""

# --- INÍCIO DO PROGRAMA ---

# Imprime um cabeçalho para o usuário saber o que o programa faz.
print("-" * 50)
print("Analisador de Frase")
print("-" * 50)

# Solicita ao usuário que insira a frase a ser analisada.
frase = input("Digite uma frase qualquer: ")

# --- Inicialização dos Contadores ---

# Define o conjunto de caracteres que serão considerados vogais.
# Inclui vogais acentuadas comuns na língua portuguesa.
VOGAIS = "aeiouáéíóúâêôãõà"

# Inicializa as variáveis que farão a contagem.
total_vogais = 0
total_brancos = 0
total_resto = 0

# --- Processamento da Frase ---

# Inicia um laço de repetição que percorre cada caractere da frase.
for caractere in frase:
    # Verifica se o caractere (convertido para minúsculo) está na string de vogais.
    if caractere.lower() in VOGAIS:
        total_vogais += 1
    # Verifica se o caractere é um espaço em branco.
    elif caractere.isspace():
        total_brancos += 1
    # Se não for vogal nem espaço, conta como 'resto'.
    else:
        total_resto += 1

# --- Exibição dos Resultados ---

# Imprime uma linha para separar a entrada da saída.
print("\n" + "=" * 50)
print("R E S U L T A D O   D A   A N Á L I S E")
print("=" * 50)

# Exibe os totais calculados para o usuário.
print(f"Total de Vogais: {total_vogais}")
print(f"Total de Espaços em Branco: {total_brancos}")
print(f"Total dos Outros Caracteres (consoantes, símbolos, etc.): {total_resto}")
print("-" * 50)