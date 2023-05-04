#027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

completo = str(input('Nome completo:')).strip()
nome = completo.split()
print('Prazer em conhecer!')
print('Seu Primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))                                                                                                                                 # O -1 é o último objeto de uma lista como -2 seria a penultima
