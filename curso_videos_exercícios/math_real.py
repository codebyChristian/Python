# Crei um programa que leia um número real e mostre na tela sua parte inteira  (Importando)

from  math import trunc
nume = float(input('Digite um número Real: '))
print('O valor digitado foi {}: e a parte inteira é {}'.format(nume, trunc(nume)))


# (Sem importação)
num = float(input('Digite um número real:'))
print('O valor digitado foi {}: a parte inteira é {}:'.format(num, int(num)))
