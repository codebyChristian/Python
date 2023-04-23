

# 039. Que leia o ano de nascimento de um jovem e informe, de acordo com idade
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Deverá mostrar o tempo que falta ou que passou do prazo
# Use o ano do sistema


print('Bem-vindo ao verificador do alistamento militar:')
ano = int(input('Digite seu ano de nascimento:'))
ano1 = 2022 - ano
print('Você tem {} anos'.format(ano1))
if ano1 >= 18:
   print('Você ainda não se alistou no serviço militar:')
   print('Já se passou \033[31m{}\033[m anos do alistamento:'.format(ano1 - 18))
else:
   print('Ainda não chegou sua vez:')
   print('Mas falta \033[34m{}\033[m anos para o alistamento:'.format(18 - ano1))

# --------------VERSÃO DIFERENTE--------------------------


from datetime import date
atual = date.today().year   # tem que criar uma varialvel
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
   print('Você tem que se alista IMEDIATAMENTE:')
elif idade < 18:
   saldo = 18 - idade
   print('Você ainda não tem 18 anos. Ainda falta {} para o alistamento'.format(saldo))
   ano = atual + saldo
   print('Seu alistamento séra em {}'.format(ano))
elif idade > 18:   # pode usar o else
   saldo = idade - 18
   print('Você já deveria ter se alistado há {} anos'.format(saldo))
   ano = atual - saldo
   print('Seu alistamento foi em {}'.format(ano))
