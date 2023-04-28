
# Faça um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MÍRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

from datetime import date
print('CLUBE DE NATAÇÃO')
atual = date.today().year
ano = int(input('Qual é o ano de nascimento:'))
idade = atual - ano
print('Você tem {} anos.'.format(idade))
if idade <= 9:
   print('Categoria: \033[33mMIRIM\033[m')
elif idade <= 14:
   print('Categoria: \033[34mINFANTIL\033[m')
elif idade <= 19:
   print('Categoria: \033[35mJUNIOR\033[m')
elif idade <= 25:
   print('Categoria: \033[36mSÊNIOR\033[m')
elif idade > 25:
   print('Categoria: \033[37mMASTER\033[m')
