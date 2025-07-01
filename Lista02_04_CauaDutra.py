"""-------------------------------------------------------------------------------
 Título:               ---Contador de Ocorrências em um Vetor---
 Finalidade:  Este programa primeiro lê 30 números inteiros para preencher um
              vetor. Em seguida, solicita ao usuário um número inteiro (X) e
              calcula e exibe quantas vezes X aparece no vetor.
 Autor:       Cauã Dutra Lima da Silva
 Data:        23 de junho de 2025
"""

# --- INÍCIO DO PROGRAMA ---

# Imprime um cabeçalho para o usuário.
print("-" * 50)
print("Contador de Ocorrências de um Número no Vetor")
print("-" * 50)

# --- Leitura do Vetor ---
print("Primeiro, vamos preencher o vetor com 30 números.")

# Inicializa a lista que será usada como vetor.
vetor = []
# Define a quantidade de elementos a serem lidos.
tamanho_vetor = 30

# Cria um laço para ler os 30 números do usuário.
for i in range(tamanho_vetor):
    # Usa um laço infinito para garantir que o usuário digite um número válido.
    while True:
        try:
            # Solicita a entrada do número.
            entrada = input(f"Digite o {i + 1}º número de {tamanho_vetor}: ")
            # Tenta converter a entrada para inteiro.
            numero = int(entrada)
            # Adiciona o número ao vetor.
            vetor.append(numero)
            # Se a conversão for bem-sucedida, sai do laço 'while'.
            break
        except ValueError:
            # Caso o usuário não digite um número, exibe uma mensagem de erro.
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

print("\nPreenchimento do vetor concluído!")

# --- Leitura do Número X ---

# Agora, solicita o número que será buscado no vetor.
while True:
    try:
        entrada_x = input("Agora, digite o número inteiro (X) que você deseja buscar no vetor: ")
        # Tenta converter a entrada para inteiro.
        numero_x = int(entrada_x)
        break
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# --- Processamento e Contagem ---

# Utiliza o método integrado do Python .count() para contar as ocorrências.
# Este método é eficiente e percorre a lista contando quantas vezes 'numero_x' aparece.
ocorrencias = vetor.count(numero_x)

# --- Exibição do Resultado ---

# Imprime uma linha para organizar a saída.
print("\n" + "=" * 50)
print("R E S U L T A D O")
print("=" * 50)

# Exibe o vetor completo para conferência do usuário.
print(f"Vetor analisado: {vetor}")

# Apresenta o resultado final da contagem.
print(f"O número {numero_x} aparece {ocorrencias} vez(es) no vetor.")
print("=" * 50)