
"""
-------------------------------------------------------------------------------
 Título:           ---Conversor de Números Romanos para Arábicos---
 Finalidade:  Este programa converte um número escrito em algarismos romanos
              (com valor menor que 4000) para seu equivalente em arábico
              (inteiro). A lógica principal processa a string da direita
              para a esquerda para tratar corretamente os casos de adição e
              subtração.
 Autor:       Cauã Dutra Lima da Silva
 Data:        25 de junho de 2025
"""

# --- ESTRUTURA DE DADOS PARA CONVERSÃO ---

# Dicionário para mapear cada símbolo romano ao seu valor inteiro.
VALORES_ROMANOS = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}

def romano_para_arabico(romano_str):
    """
    Converte uma string em algarismo romano para um número inteiro.
    Retorna o número ou None se a entrada for inválida.
    """
    # Garante que a entrada esteja em maiúsculas para o mapeamento.
    romano_str = romano_str.upper()
    
    # Validação: verifica se todos os caracteres na string são válidos.
    for char in romano_str:
        if char not in VALORES_ROMANOS:
            return None # Retorna None para indicar entrada inválida.

    total = 0
    valor_anterior = 0

    # Itera sobre a string romana EM ORDEM REVERSA (da direita para a esquerda).
    for char in reversed(romano_str):
        valor_atual = VALORES_ROMANOS[char]
        
        # Se o valor atual for maior ou igual ao anterior, soma ao total.
        # Exemplo: Em "VI", processa I (1), depois V (5). Como 5 >= 1, soma-se 5.
        if valor_atual >= valor_anterior:
            total += valor_atual
        # Se for menor, subtrai do total.
        # Exemplo: Em "IV", processa V (5), depois I (1). Como 1 < 5, subtrai-se 1.
        else:
            total -= valor_atual
            
        # Atualiza o valor anterior para a próxima iteração.
        valor_anterior = valor_atual
        
    return total

# --- PROGRAMA PRINCIPAL (MENU INTERATIVO) ---

print("=" * 60)
print("     Conversor de Números Romanos para Arábicos")
print("=" * 60)

# Laço principal para permitir múltiplas conversões.
while True:
    entrada_usuario = input("\nDigite um número romano (ex: MCMXCIV) ou 'sair' para fechar: ")

    # Condição de saída do programa.
    if entrada_usuario.lower() == 'sair':
        print("\nObrigado por usar o conversor. Até logo!")
        break

    # Chama a função de conversão.
    resultado = romano_para_arabico(entrada_usuario)
    
    # Verifica o resultado da função.
    if resultado is not None:
        # Validação adicional para a regra de < 4000
        if resultado < 4000:
            print(f" -> O número romano '{entrada_usuario.upper()}' corresponde a: {resultado}")
        else:
            print(f"Erro: O número romano '{entrada_usuario.upper()}' ({resultado}) é igual ou maior que 4000.")
    else:
        # Mensagem de erro se a entrada contiver caracteres inválidos.
        print(f"Erro: '{entrada_usuario}' contém caracteres que não são algarismos romanos válidos.")

print("\n" + "=" * 60)