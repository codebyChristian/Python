# Exercicio 4

def exercicio3 (dados):
    for i in range(0, len(dados), 1):
        for j in range(i, len(dados), 1):
            dados[i] = dados[j] + 1

# Esse é uma função com dois laços for aninhados começando em i
# Neste exemplo é uma PA de -1, portanto a complexidade é: O(n²)