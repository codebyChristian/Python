# Exercicio 2

def exercico2 (dados):
    for i in range(0, len(dados), 1):
        dados[i] = i + 1
    for i in range(0, len(dados), 1):
        dados[i] = i - 1

# Essa função com 2 laços de repetição, utiliza a propriedade da adição
# A complexidade será: O(n)