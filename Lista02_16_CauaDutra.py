"""
-------------------------------------------------------------------------------
 Título:           ---Enumerador de Subsequências Não Contínuas---
 Finalidade:  Este programa recebe uma sequência de elementos e encontra todas
              as suas subsequências não contínuas. Uma subsequência é não
              contínua se, na sequência original, existe algum elemento
              faltando entre o primeiro e o último membro da subsequência.
 Autor:       Cauã Dutra Lima da Silva
 Data:        25 de junho de 2025
"""

def eh_continua(subsequencia, sequencia_original):
    """
    Verifica se uma dada subsequência é contínua em relação à original.
    
    Ex: Para a original (1,2,3,4):
        - (2,3) é contínua, pois na original não falta nada entre 2 e 3.
        - (2,4) NÃO é contínua, pois na original falta o 3 entre 2 e 4.
    
    :param subsequencia: A subsequência a ser testada.
    :param sequencia_original: A sequência completa de referência.
    :return: True se for contínua, False caso contrário.
    """
    # Subsequências com menos de 2 elementos são trivialmente contínuas.
    if len(subsequencia) < 2:
        return True

    # Encontra os índices do primeiro e do último elemento da subsequência na original.
    try:
        inicio_idx = sequencia_original.index(subsequencia[0])
        fim_idx = sequencia_original.index(subsequencia[-1])
    except ValueError:
        # Isso não deve acontecer se a subsequência for válida, mas é uma segurança.
        return False

    # Extrai o "pedaço" correspondente da sequência original.
    fatia_original = sequencia_original[inicio_idx : fim_idx + 1]

    # A subsequência é contínua se ela for idêntica à fatia da original.
    return list(subsequencia) == list(fatia_original)


def encontrar_subsequencias_nao_continuas(sequencia):
    """
    Encontra e retorna todas as subsequências não contínuas de uma sequência.
    """
    n = len(sequencia)
    todas_as_subsequencias = []

    # Passo 1: Gerar TODAS as subsequências possíveis usando bitmasking.
    # Para uma sequência de tamanho n, existem 2^n subsequências.
    # Cada número de 0 a 2^n - 1 pode ser usado como uma "máscara" binária.
    for i in range(1, 1 << n):  # 1 << n é o mesmo que 2^n
        subsequencia_atual = []
        for j in range(n):
            # Se o j-ésimo bit de i estiver "ligado" (for 1)...
            if (i >> j) & 1:
                # ...incluímos o j-ésimo elemento da sequência original.
                subsequencia_atual.append(sequencia[j])
        
        todas_as_subsequencias.append(subsequencia_atual)

    # Passo 2: Filtrar a lista, mantendo apenas as não contínuas.
    resultado_final = []
    for sub in todas_as_subsequencias:
        # A condição de filtro: ser não contínua e ter pelo menos 2 elementos.
        if len(sub) >= 2 and not eh_continua(sub, sequencia):
            resultado_final.append(sub)
            
    return resultado_final


# --- Bloco Principal para Execução e Teste ---
if __name__ == "__main__":
    print("=" * 60)
    print("     Enumerador de Subsequências Não Contínuas")
    print("=" * 60)

    # Sequência de exemplo fornecida na questão.
    sequencia_teste = (1, 2, 3, 4)
    
    print(f"Analisando a sequência: {sequencia_teste}\n")

    # Chama a função principal para obter o resultado.
    subsequencias_encontradas = encontrar_subsequencias_nao_continuas(sequencia_teste)

    print("Subsequências não contínuas encontradas:")
    # Imprime o resultado final, que deve ser idêntico ao do exemplo.
    print(subsequencias_encontradas)

    print("\n--- Outro Exemplo ---")
    sequencia_teste_2 = ('A', 'B', 'C')
    print(f"Analisando a sequência: {sequencia_teste_2}\n")
    subsequencias_encontradas_2 = encontrar_subsequencias_nao_continuas(sequencia_teste_2)
    print("Subsequências não contínuas encontradas:")
    print(subsequencias_encontradas_2) # Deve ser [['A', 'C']]
    
    print("\n" + "=" * 60)