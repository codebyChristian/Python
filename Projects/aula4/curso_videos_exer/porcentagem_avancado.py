

# Leia o preço de um produto e mostre as condições de pagamenrtos
# Á vista dinheiro/cheque: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juras

print('VEJA AS CONDIÇÕES DE PAGAMENTOS\n'
      'DIGITE O NÚMERO CORRESPONTENTE....\n'
      '1: PARA PAGAMENTOS Á VISTA EM DINHEIRO OU CHEQUE: 10% DE DESCONTO\n'
      '2: PARA PAGEMENTOS Á VISTA NO CARTÃO: 5% DE DESCONTO\n'
      '3: PARA PAGAMENTOS EM ATÉ 2 VEZES: PREÇO NORMAL\n'
      '4: PARA PAGAMENTOS ACIMA DE 3 VEZES: 20% DE JUROS\n')
produto = float(input('Qual é valor do produto? R$'))
numero = int(input('Qual a condição desejada: '))
desconto1 = produto - (produto * 0.10)   # 10% de desonto
desconto2 = produto - (produto * 0.05)   # 5% de desconto
if numero == 1:
    print('Parabéns! O valor deixou de ser de {:.2f}R$ para \033[31m{:.2f}R$\033[m'.format(produto, desconto1))
elif numero == 2:
    print('Parabéns! O valor deixou de ser de {:.2f}R$ para \033[32m{:.2f}R$\033[m'.format(produto, desconto2))
elif numero == 3:
    total = produto
    parcela = total / 2
    print('O valor será 2x de R$\033[33m{:.2f}\033[m '.format(parcela))
elif numero == 4:
    meses = int(input('Em quantas vezes você irá pagar? '))
    juros = produto + (produto * 0.20)
    parcela = juros / meses
    print('Sua compra será parcelada em {}x de {:.2f} no final.'.format(meses, parcela))
else:
    print('\033[35mNÚMERO INVALIDO...\033[m')
