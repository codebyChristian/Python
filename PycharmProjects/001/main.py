km = int(input('Quantos quilometros rodados?'))
dias = int(input('Quantos dias o carro ficou contigo?'))

# 60 reias por dia e 0.15 por km
preco = 60 * dias + 0.15 * km
print('{}Km rodados. Em {} Dias'.format(km, dias))
print('O valor a ser pago é {}'.format(preco))
