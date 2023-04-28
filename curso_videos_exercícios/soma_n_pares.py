# Leia seis números inteiros e mostre apenas daqueles que forem pares e some todos
# Se o valor digitado for ímpar, desconsidere-o

soma = 0
cont = 0
for i in range(1, 7, 1):
    number = int(input('Digite o {} valor. > '.format(i)))
    if number % 2 == 0:
        soma += number
        cont += 1
print('Você informou {} números PARES e a soma é {}'.format(cont, soma))         # O print é sempre fora da ententação

