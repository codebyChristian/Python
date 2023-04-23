
# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date
ano = int(input('Digite qualquer ano >  Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year   # Pegar o ano atual da máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # È divisivel por 4 exceto por 100 e 400
    print('O ano {} é BISSEXTO:'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))