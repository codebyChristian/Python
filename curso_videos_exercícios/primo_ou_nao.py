# Faça um programa que leia um número inteiro e diga se ele é ou não primo

# REFAÇA ------------------------

numero = int(input('Digite qualquer número. > '))
total = 0   # Para saber quantas vezes foi divisivel
for primo in range(1, numero + 1):
    if numero % primo == 0:
        print('\033[37m', end=' ')
        total += 1
    else:
        print('\033[34m', end=' ')
    print('{}'.format(primo), end=' ')
print('\n\033[mO número {} foi divisivel {} vezes'.format(numero, total))
if total == 2:
    print('\033[31mEsse númeroé primo\033[m')
else:
    print('Esse número Não é primo')

