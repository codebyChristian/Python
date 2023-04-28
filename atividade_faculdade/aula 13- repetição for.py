for c in range(1, 7):
    print('Hello, Word')
print('The End')

for c in range(6, 0, -2):  # Contagem inversa
    print(c)

n = int(input('Digite um número:'))
for c in range(0, n):
    print(c)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)


s = 0  # Para somar é preciso colocar uma variável fora do laço para contar
for c in range(0, 3):
    n = int(input('Digite um valor: '))   # Repete quantas vezes quiser
    s = s + n
print('A soma dos números é \033[31m{}\033[m'.format(s))


