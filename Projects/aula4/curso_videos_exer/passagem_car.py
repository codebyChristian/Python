
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule e peça o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R#0,45
# para viagens mais longas

distan = float(input('Qual a distância de sua viagem > '))
if distan <= 200:
    valor = distan * 0.50
    print('O valor a ser pago em é {:.2f} Reais'.format(valor))
else:
    conta = distan * 0.45
    print('O valor a ser pago em é {:.2f} Reais'.format(conta))

# -------------SIMPLIFICADA------------
distan = float(input('Qual a distância de sua viagem > '))
preco = distan * 0.50 if distan <= 200 else distan * 0.45
print('E o preço de sua passagem será RS{:.2f}'.format(preco))