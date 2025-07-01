'''
# Titulo:                  ---Analisador de Temperaturas---
# FINALIDADE: Este programa lê 50 temperaturas em graus Celsius, converte
#             essas temperaturas para Farenheit, e ao final, exibe a média
#             em ambas as escalas e a contagem de temperaturas em Farenheit
#             que ficaram acima da média.
#
# AUTOR: [Cauã Dutra Lima da Silva]
# DATA DE CRIAÇÃO: 23/06/2025
'''



def converter_celsius_para_farenheit(temp_celsius):
    """
    Converte uma única temperatura da escala Celsius para Farenheit.
    A fórmula utilizada é F = (C * 9/5) + 32.
    """
    return (temp_celsius * 9/5) + 32

# --- PROGRAMA PRINCIPAL ---
if __name__ == "__main__":

    # Define a quantidade de temperaturas que devem ser lidas.
    TOTAL_DE_LEITURAS = 50

    # Inicializa as listas que irão armazenar os valores de temperatura.
    temperaturas_celsius = []
    temperaturas_farenheit = []

    print(f"Por favor, insira {TOTAL_DE_LEITURAS} valores de temperatura em graus Celsius.")

    # Inicia o loop para coletar os 50 valores do usuário.
    for i in range(TOTAL_DE_LEITURAS):
        # Este loop 'while' garante que o usuário digite um número válido.
        while True:
            try:
                # Solicita a entrada e tenta convertê-la para um número (float).
                entrada_temp_c = float(input(f"Digite a temperatura Nº {i+1}: "))
                temperaturas_celsius.append(entrada_temp_c)
                break  # Se a entrada for válida, sai do loop 'while'.
            except ValueError:
                # Mensagem de erro caso a entrada não seja um número.
                print("Entrada inválida. Por favor, digite um valor numérico.")

    # Confere se a lista de temperaturas não está vazia para evitar erros.
    if temperaturas_celsius:
        # Loop para converter cada temperatura de Celsius e popular a lista Farenheit.
        for temp_c in temperaturas_celsius:
            temp_f = converter_celsius_para_farenheit(temp_c)
            temperaturas_farenheit.append(temp_f)

        # --- CÁLCULO DAS ESTATÍSTICAS ---

        # Calcula a média das temperaturas em Celsius.
        media_celsius = sum(temperaturas_celsius) / len(temperaturas_celsius)

        # Calcula a média das temperaturas em Farenheit.
        media_farenheit = sum(temperaturas_farenheit) / len(temperaturas_farenheit)

        # Inicializa o contador para as temperaturas acima da média.
        contador_acima_media_f = 0

        # Loop para verificar cada temperatura em Farenheit.
        for temp_f in temperaturas_farenheit:
            # Se a temperatura for maior que a média, incrementa o contador.
            if temp_f > media_farenheit:
                contador_acima_media_f += 1

        # --- EXIBIÇÃO DOS RESULTADOS ---

        # Imprime o relatório final de forma organizada.
        print("\n" + "="*35)
        print("      ANÁLISE DAS TEMPERATURAS")
        print("="*35)
        print(f"Média em Celsius: {media_celsius:.2f}°C")
        print(f"Média em Farenheit: {media_farenheit:.2f}°F")
        print(f"Temperaturas acima da média em Farenheit: {contador_acima_media_f}")
        print("="*35)

    else:
        # Mensagem caso nenhum dado tenha sido inserido.
        print("Nenhuma temperatura foi inserida para análise.")