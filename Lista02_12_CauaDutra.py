"""
-------------------------------------------------------------------------------
 Título:              ---Inversor de Caixa de Texto em uma String---
 Finalidade:  Este programa utiliza um texto (string) pré-definido no código,
              troca todas as letras minúsculas por maiúsculas e vice-versa,
              e imprime o resultado diretamente na tela.
 Autor:       Cauã Dutra Lima da Silva
 Data:        24 de junho de 2025
"""

print("=" * 60)
print("   Inversor de Caixa de Texto (versão interativa)")
print("=" * 60)

# --- 1. Entrada de Dados pelo Usuário ---

# Fornece instruções claras para o usuário.
print("Digite o texto que deseja transformar. Pressione Enter para ir para a próxima linha.")
print("Quando terminar, deixe uma linha em branco e pressione Enter novamente.")
print("----------------------------------------------------------------")

# Lista para armazenar cada linha digitada pelo usuário.
linhas_do_texto = []

# Laço infinito que só será quebrado quando o usuário terminar a entrada.
while True:
    # Lê uma linha do console.
    linha = input()
    
    # Verifica a condição de parada: uma linha vazia.
    if linha == "":
        break
    else:
        # Adiciona a linha digitada à nossa lista.
        linhas_do_texto.append(linha)

# Junta todas as linhas da lista em uma única string,
# separando-as com o caractere de quebra de linha '\n'.
texto_original = "\n".join(linhas_do_texto)


# --- 2. Processamento e Exibição ---

# Verifica se o usuário de fato digitou algo.
if not texto_original:
    print("\nNenhum texto foi digitado. Encerrando o programa.")
else:
    # Mostra o texto original que foi capturado.
    print("\n--- Texto Original Digitado ---")
    print(texto_original)

    # A lógica de inversão continua a mesma: o método .swapcase()
    texto_invertido = texto_original.swapcase()

    # O resultado é impresso na tela.
    print("\n--- Texto com Caixa Invertida ---")
    print(texto_invertido)

print("\n" + "=" * 60)
print("Operação concluída.")