# Exercicio 5

def exercicio5 (dados):
    for i in range(0, len(dados), 1):
        for j in range(0, len(dados), 1):
            for k in range(0, 9000000, 1):
                dados[i] = dados[j] + 1

# Esse é uma função com 3 laços for aninhados 
# A complexidade é: T(n) = 9000000 * n * = O(n²)