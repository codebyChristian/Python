#025: Crie um programa que leia o nome de uma pessoa e
# diga se ela tem "SILVA" no nome.

pessoa = str(input('Escreva um nome:')).strip() 
print('SILVA' in pessoa.upper())


# DICAS DO PROFESSOR
#nome = input('Qual seu nome:')
#print('seu nome tem Silva? {}'.format('silva' in nome.lower()))
