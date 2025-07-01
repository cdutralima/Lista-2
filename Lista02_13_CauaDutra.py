"""
-------------------------------------------------------------------------------
 Título:           ---Conversor de Números Arábicos para Romanos---
 Finalidade:  Este programa converte um número inteiro (entre 1 e 3999)
              fornecido pelo usuário para seu equivalente em algarismos romanos.
              A lógica evita o uso excessivo de condicionais 'if', optando por
              uma abordagem de mapeamento e subtração.
 Autor:       Cauã Dutra Lima da Silva
 Data:        25 de junho de 2025
"""
def converter_para_romano_v2(numero):
    """
    Converte um número para romano analisando cada casa decimal.
    """
    # A estrutura armazena os símbolos para cada casa decimal.
    # Posição 0: Unidades (I, V, X)
    # Posição 1: Dezenas (X, L, C)
    # Posição 2: Centenas (C, D, M)
    # Posição 3: Milhares (M, -, -)
    simbolos_por_casa = [
        ('I', 'V', 'X'),  # Unidades
        ('X', 'L', 'C'),  # Dezenas
        ('C', 'D', 'M'),  # Centenas
        ('M', '', '')     # Milhares
    ]

    partes_romanas = []
    casa_decimal = 0

    # O laço 'while' analisa o número da direita para a esquerda (unidade, dezena...).
    while numero > 0:
        # 1. Pega o último dígito do número (ex: de 123, pega o 3).
        ultimo_digito = numero % 10
        
        # 2. Pega os símbolos correspondentes à casa decimal atual.
        um, cinco, dez = simbolos_por_casa[casa_decimal]
        
        # 3. Converte o dígito (0-9) para a representação romana.
        #    Esta estrutura de 'if's é compacta e respeita o limite.
        parte = ''
        if ultimo_digito == 9:
            parte = um + dez          # Ex: 9 -> IX
        elif ultimo_digito >= 5:
            parte = cinco + um * (ultimo_digito - 5)  # Ex: 7 -> VII
        elif ultimo_digito == 4:
            parte = um + cinco        # Ex: 4 -> IV
        else: # Casos 1, 2, 3
            parte = um * ultimo_digito # Ex: 3 -> III
        
        # 4. Adiciona a parte convertida no INÍCIO da lista de resultados.
        partes_romanas.insert(0, parte)
        
        # 5. Prepara para a próxima iteração.
        casa_decimal += 1         # A próxima casa será dezena, depois centena...
        numero //= 10             # Remove o último dígito do número (ex: 123 vira 12).
        
    # 6. Junta todas as partes para formar o número romano final.
    return "".join(partes_romanas)

# --- PROGRAMA PRINCIPAL (MENU INTERATIVO - SEM ALTERAÇÕES) ---

print("=" * 60)
print("     Conversor de Números Arábicos para Romanos (v2)")
print("=" * 60)

while True:
    entrada_usuario = input("\nDigite um número entre 1 e 3999 (ou digite 'sair' para fechar): ")

    if entrada_usuario.lower() == 'sair':
        print("\nObrigado por usar o conversor. Até logo!")
        break

    try:
        numero_int = int(entrada_usuario)
        
        if 1 <= numero_int < 4000:
            # Chama a NOVA função de conversão.
            romano = converter_para_romano_v2(numero_int)
            print(f" -> O número {numero_int} em algarismos romanos é: {romano}")
        else:
            print("Erro: Por favor, digite um número estritamente entre 1 e 3999.")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número.")

print("\n" + "=" * 60)