# Fornecimento de energia
kwh = float(input('Qual a quantidade gasta: '))
tipo = input('Qual sua instalação: I, C, R.')
if (tipo == 'R'):
    if kwh <= 500:
        preco = 0.4
    else:
        preco = 0.65
elif (tipo == 'C'):
    if kwh <= 1000:
        preco = 0.55
    else:
        preco = 0.6
elif (tipo == 'I'):
    if kwh <= 5000:
        preco = 0.55
    else:
        preco = 0.6

else:
    print('Istalação invalida:')
print('Total a pagar: {}$ Reais'.format(kwh * preco))