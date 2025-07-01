"""
-------------------------------------------------------------------------------
 Título:          ---Gerador dos N Primeiros Números Primos---
 Finalidade:  Este programa solicita ao usuário um número inteiro N e, em
              seguida, calcula e imprime os N primeiros números primos.
 Autor:       Cauã Dutra Lima da Silva
 Data:        24 de junho de 2025
"""

# Importa o módulo 'math' para usar a função de raiz quadrada (sqrt) na
# otimização da verificação de primos.
import math

def eh_primo(numero):
    """
    Função auxiliar que verifica se um número é primo.
    Retorna True se o número for primo, e False caso contrário.
    A verificação é otimizada para maior eficiência.
    """
    # Números menores ou iguais a 1 não são primos.
    if numero <= 1:
        return False
    # O número 2 é o único primo par.
    if numero == 2:
        return True
    # Todos os outros números pares não são primos.
    if numero % 2 == 0:
        return False
    # Verifica divisores ímpares a partir de 3 até a raiz quadrada do número.
    # Se um número tem um divisor maior que sua raiz quadrada, ele também
    # terá um divisor menor. Por isso, não precisamos testar além disso.
    limite = int(math.sqrt(numero))
    for i in range(3, limite + 1, 2):
        if numero % i == 0:
            return False
    # Se nenhum divisor for encontrado, o número é primo.
    return True

# --- INÍCIO DO PROGRAMA PRINCIPAL ---

# Imprime um cabeçalho para o usuário.
print("-" * 50)
print("     Gerador dos N Primeiros Números Primos")
print("-" * 50)

# --- Leitura da Quantidade de Primos (N) ---

# Solicita ao usuário a quantidade de números primos a serem gerados.
while True:
    try:
        n = int(input("Quantos números primos você deseja encontrar? "))
        if n >= 0:
            break
        else:
            print("Erro: Por favor, digite um número não negativo (0 ou mais).")
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro.")

# --- Geração e Impressão dos Números Primos ---

# Inicializa a lista que armazenará os números primos encontrados.
primos_encontrados = []
# Começa a testar os números a partir do 2.
numero_atual = 2

# Imprime uma mensagem indicando o início do processo, útil para N grande.
if n > 0:
    print(f"\nCalculando os {n} primeiros números primos... Por favor, aguarde.")

# Continua o laço até que a lista tenha 'n' números primos.
while len(primos_encontrados) < n:
    # Usa a função auxiliar para verificar se o número atual é primo.
    if eh_primo(numero_atual):
        # Se for primo, adiciona à lista.
        primos_encontrados.append(numero_atual)
    
    # Passa para o próximo número a ser testado.
    numero_atual += 1

# --- Exibição do Resultado ---

# Imprime uma linha para organizar a saída.
print("\n" + "=" * 50)
print("R E S U L T A D O")
print("=" * 50)

# Exibe a lista final com os primos encontrados.
if n == 0:
    print("Nenhum número primo foi solicitado.")
else:
    print(f"Os {n} primeiros números primos são:")
    print(primos_encontrados)

print("=" * 50)