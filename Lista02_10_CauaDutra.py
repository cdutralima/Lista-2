"""
-------------------------------------------------------------------------------
 Título:             ---Contador de Frequência de Palavras---
 Finalidade:  Este programa lê 'texto.txt', remove pontuações e números,
              e conta a frequência de cada palavra usando duas listas
              paralelas (uma para palavras, outra para contagens).
 Autor:       Cauã Dutra Lima da Silva
 Data:        24 de junho de 2025
"""

# Importa o módulo 'string' para obter uma lista de pontuações comuns.
import string

def limpar_palavra(palavra_suja):
    """
    Função auxiliar para limpar uma única palavra.
    - Converte para minúsculas.
    - Remove pontuações do início e do fim.
    """
    palavra_limpa = palavra_suja.lower()
    palavra_limpa = palavra_limpa.strip(string.punctuation)
    return palavra_limpa

# --- INÍCIO DO PROGRAMA PRINCIPAL ---

print("=" * 60)
print("     Contador de Frequência de Palavras (Versão com Listas)")
print("=" * 60)

# Inicializa as listas paralelas.
# 'palavras_unicas' armazenará cada palavra diferente encontrada.
# 'contagens' armazenará a frequência da palavra no mesmo índice.
palavras_unicas = []
contagens = []

nome_arquivo = 'texto.txt'

# --- Leitura e Processamento do Arquivo ---
try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            palavras_na_linha = linha.split()
            
            for palavra_suja in palavras_na_linha:
                palavra = limpar_palavra(palavra_suja)
                
                # Continua apenas se a palavra for válida (não vazia e não número).
                if palavra and not palavra.isdigit():
                    # Verifica se a palavra já foi adicionada à nossa lista de palavras únicas.
                    if palavra in palavras_unicas:
                        # Se já existe, encontra seu índice.
                        indice = palavras_unicas.index(palavra)
                        # Incrementa a contagem no mesmo índice na lista de contagens.
                        contagens[indice] += 1
                    else:
                        # Se é uma palavra nova, adiciona-a à lista de palavras únicas.
                        palavras_unicas.append(palavra)
                        # Adiciona uma nova contagem (iniciando em 1) na lista de contagens.
                        contagens.append(1)

    # --- Exibição dos Resultados ---
    
    if not palavras_unicas:
        print("\nNenhuma palavra válida foi encontrada no arquivo para contagem.")
    else:
        # Para ordenar, primeiro combinamos as duas listas em pares (palavra, contagem).
        # A função zip() faz exatamente isso.
        pares_palavra_contagem = list(zip(palavras_unicas, contagens))
        
        # Agora, ordenamos a lista de pares com base na contagem (o segundo item do par).
        itens_ordenados = sorted(pares_palavra_contagem, key=lambda item: item[1], reverse=True)
        
        print(f"\nFrequência de cada palavra encontrada no arquivo '{nome_arquivo}':")
        print("-------------------------------------------------")
        print(f"{'Palavra':<20} | {'Ocorrências'}")
        print("-------------------------------------------------")
        
        for palavra, contagem in itens_ordenados:
            print(f"{palavra:<20} | {contagem}")
        print("-------------------------------------------------")

except FileNotFoundError:
    print(f"\n[ERRO FATAL]")
    print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    print("Por favor, crie o arquivo na mesma pasta do script e tente novamente.")

except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")