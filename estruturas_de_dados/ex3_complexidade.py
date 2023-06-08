# Exercicio3

def exercicio3 (dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            dados[i] = dados[j] + 1

# Esse é uma função com dois laços for aninhados
# Neste exemplo é uma PA constante, portanto a complexidade é: O(n²)