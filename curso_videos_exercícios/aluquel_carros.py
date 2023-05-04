# Aluquel de carros: preço dia: 60 reias, preço km: 0.15


print('Aluguel de Carros')
kilo = float(int(input('Quantos Quilômetros perroridos:>')))
dias = int(input('Quantos dias de uso:>'))
preco = 60 * dias + 0.15 * kilo
print('Você rodou {}Km, e usou o carro em {}dia(s): Então o preço será R${:.2f}'.format(kilo,dias,preco))
