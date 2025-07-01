
"""
-------------------------------------------------------------------------------
 Título:                ---Simulador de Caixa Eletrônico---
 Finalidade:  Este programa simula um caixa eletrônico que calcula a menor
              quantidade de notas para um saque, considerando um estoque
              limitado de cédulas. O estoque é atualizado após cada saque
              bem-sucedido. O programa informa caso o saque não seja
              possível por falta de notas específicas ou de saldo total.
 Autor:       Cauã Dutra Lima da Silva
 Data:        24 de junho de 2025
"""
# --- ESTADO INICIAL DO CAIXA ELETRÔNICO (usando listas paralelas) ---

# Lista que armazena os valores de cada tipo de nota. Esta lista não muda.
# A ordem decrescente é essencial para o funcionamento do algoritmo.
NOTAS_VALORES = [100, 50, 20, 10, 5, 1]

# Lista que armazena a quantidade de cada nota.
# A posição (índice) corresponde à mesma posição em NOTAS_VALORES.
# Ex: estoque_quantidades[0] é a quantidade de notas de R$100.
# Esta lista será modificada a cada saque.
estoque_quantidades = [10, 10, 10, 10, 10, 10]

# --- FUNÇÕES ---

def mostrar_estoque():
    """Exibe a quantidade atual de cada nota no caixa."""
    print("\n--- Estoque Atual de Notas ---")
    total_disponivel = 0
    # Itera sobre os índices das listas.
    for i in range(len(NOTAS_VALORES)):
        valor_nota = NOTAS_VALORES[i]
        quantidade = estoque_quantidades[i]
        print(f"Notas de R$ {valor_nota:3}: {quantidade:2} unidades")
        total_disponivel += valor_nota * quantidade
    print("--------------------------------")
    print(f"Valor Total Disponível: R$ {total_disponivel:.2f}")
    print("--------------------------------")


def realizar_saque():
    """Função principal que gerencia a lógica de saque."""
    global estoque_quantidades

    # --- Leitura do Valor ---
    try:
        valor_saque = int(input("\nDigite o valor que deseja sacar: R$ "))
        if valor_saque <= 0:
            print("Erro: O valor do saque deve ser um número positivo.")
            return
    except ValueError:
        print("Erro: Valor inválido. Por favor, digite um número inteiro.")
        return

    # --- Verificação Preliminar de Saldo ---
    total_disponivel = 0
    for i in range(len(NOTAS_VALORES)):
        total_disponivel += NOTAS_VALORES[i] * estoque_quantidades[i]
    
    if valor_saque > total_disponivel:
        print("\n[OPERAÇÃO CANCELADA]")
        print(f"Não há dinheiro suficiente no caixa para sacar R$ {valor_saque:.2f}.")
        print(f"Valor máximo disponível: R$ {total_disponivel:.2f}")
        return

    # --- Lógica de Distribuição das Notas ---

    valor_restante = valor_saque
    # Cria uma lista para planejar a entrega, inicializada com zeros.
    notas_a_entregar = [0] * len(NOTAS_VALORES)

    # Itera sobre os índices das listas de notas, da maior para a menor.
    for i in range(len(NOTAS_VALORES)):
        valor_nota = NOTAS_VALORES[i]
        
        if valor_restante >= valor_nota:
            qtd_necessaria = valor_restante // valor_nota
            qtd_disponivel = estoque_quantidades[i]
            qtd_a_usar = min(qtd_necessaria, qtd_disponivel)
            
            if qtd_a_usar > 0:
                notas_a_entregar[i] = qtd_a_usar
                valor_restante -= qtd_a_usar * valor_nota

    # --- Validação e Conclusão do Saque ---

    if valor_restante > 0:
        print("\n[OPERAÇÃO CANCELADA]")
        print("Não é possível formar o valor solicitado com as notas disponíveis no momento.")
        print("Tente um valor diferente.")
    else:
        print("\n[SAQUE APROVADO]")
        print("Por favor, retire as notas abaixo:")
        print("--------------------------------")
        for i in range(len(NOTAS_VALORES)):
            if notas_a_entregar[i] > 0:
                valor_nota = NOTAS_VALORES[i]
                quantidade_entregue = notas_a_entregar[i]
                print(f"-> {quantidade_entregue} nota(s) de R$ {valor_nota}")
                # Efetiva a retirada das notas do estoque principal.
                estoque_quantidades[i] -= quantidade_entregue
        print("--------------------------------")
        print("Obrigado por usar nossos serviços!")


# --- PROGRAMA PRINCIPAL ---

print("=" * 50)
print("     BEM-VINDO AO CAIXA ELETRÔNICO     ")
print("=" * 50)

while True:
    print("\nEscolha uma opção:")
    print("  1 - Realizar Saque")
    print("  2 - Verificar Estoque de Notas")
    print("  3 - Sair")
    
    opcao = input("Opção: ")

    if opcao == '1':
        realizar_saque()
    elif opcao == '2':
        mostrar_estoque()
    elif opcao == '3':
        print("\nEncerrando o sistema. Até logo!")
        break
    else:
        print("\nOpção inválida. Por favor, tente novamente.")