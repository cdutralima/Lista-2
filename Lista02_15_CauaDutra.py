"""
-------------------------------------------------------------------------------
 Título:               ---Decomposição em Fatores Primos---
 Finalidade:  Este programa contém uma função, fat_primo(num), que recebe um
              número inteiro e o decompõe em seus fatores primos, retornando
              um vetor (lista) com a decomposição no formato 'primo^expoente'.
 Autor:       Cauã Dutra Lima da Silva
 Data:        25 de junho de 2025
"""

def fat_primo(num):
    """
    Decompõe um número inteiro em seus fatores primos.
    :param num: O número inteiro a ser decomposto.
    :return: Uma lista de strings com os fatores primos e seus expoentes.
             Ex: ['2^3', '3^1', '5^2']
    """
    # Validação de entrada: números menores que 2 não têm decomposição em primos.
    if not isinstance(num, int) or num < 2:
        return []

    # Um dicionário é ideal para armazenar os fatores e contar seus expoentes.
    fatores = {}
    
    # --- Passo 1: Lidar com o fator 2 ---
    # Divide o número por 2 quantas vezes for possível.
    while num % 2 == 0:
        fatores[2] = fatores.get(2, 0) + 1
        num //= 2
    
    # --- Passo 2: Lidar com fatores ímpares ---
    # Após remover todos os fatores 2, o número restante é ímpar.
    # Podemos então pular os números pares em nossa busca por fatores.
    # A busca só precisa ir até a raiz quadrada do número restante.
    fator_impar = 3
    while fator_impar * fator_impar <= num:
        while num % fator_impar == 0:
            fatores[fator_impar] = fatores.get(fator_impar, 0) + 1
            num //= fator_impar
        fator_impar += 2 # Pula para o próximo número ímpar.

    # --- Passo 3: Lidar com o número restante ---
    # Se, após todas as divisões, o número restante for maior que 2,
    # significa que ele mesmo é um fator primo.
    if num > 2:
        fatores[num] = fatores.get(num, 0) + 1

    # --- Passo 4: Formatar a saída ---
    # Cria a lista de strings no formato 'primo^expoente'.
    # Usamos sorted(fatores.keys()) para garantir que a saída seja ordenada.
    resultado_formatado = []
    for fator in sorted(fatores.keys()):
        expoente = fatores[fator]
        resultado_formatado.append(f"{fator}^{expoente}")
        
    return resultado_formatado

# --- Bloco Principal para Teste Interativo ---
if __name__ == "__main__":
    print("=" * 60)
    print("     Decomposição de um Número em Fatores Primos")
    print("=" * 60)

    while True:
        entrada = input("\nDigite um número inteiro (ou 'sair' para fechar): ")
        if entrada.lower() == 'sair':
            print("\nEncerrando o programa.")
            break
        
        try:
            numero_para_decompor = int(entrada)
            decomposicao = fat_primo(numero_para_decompor)
            
            if not decomposicao:
                print(f" -> O número {numero_para_decompor} não pode ser decomposto em fatores primos.")
            else:
                # O método ' '.join() junta os elementos da lista em uma única string.
                print(f" -> A decomposição de {numero_para_decompor} é: {' * '.join(decomposicao)}")

        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número inteiro.")
    
    print("\n" + "=" * 60)