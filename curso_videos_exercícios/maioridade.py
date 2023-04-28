# Leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas
# ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pess in range(1, 8):
    idade = int(input('Digite seu ano de nascimento da {}* pessoa: > '.format(pess)))
    nasc = atual - idade
    if nasc >= 18:
        totalmaior += 1
    else:
        totalmenor += 1
print('Ao todo \033[31mtemos {} pessoas maior de idade\033[m e \033[37m{} menor de idade\033[m.'.format(totalmaior, totalmenor))

# refaça
