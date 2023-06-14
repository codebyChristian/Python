
import random

def buscaBinaria (inicio, fim, dados, buscado):
    while(inicio <= fim):
        meio = int((inicio + fim)/2)
        if (buscado > dados[meio]):
            inicio = meio + 1
        elif (buscado < dados[meio]):
            fim = meio - 1
        else: 
            return meio
    return -1

# Principal
#Valores de 0 até 9

dados = random.sample(range(10), 10)
dados.sort()
print(dados)
buscado = int(input("Digite o valor que deseja buscar: "))
achou = buscaBinaria(0, len(dados), dados, buscado)

