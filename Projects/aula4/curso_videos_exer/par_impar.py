#Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

nume = int(input('Digite qualquer número >'))
if nume % 2 == 0:     # % é resto de devisão
    print('O número {} é PAR'.format(nume))   # Resto de divisão é 0
else:
    print('O número {} é ÍMPAR'.format(nume))  # Resto de divisão é 1