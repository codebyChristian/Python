# refaça dsf 51, lendo umtermo e a razão de uma PA,
# Mostrando os 10 primeiros termos da progressão usando while
# Tempo 32:08

print('Gerador de P.A')
termo = int(input('Qual termo será usado > '))
razao = int(input('Qual a razão: > '))
primeiro = termo   # Mostra o termo
cont = 1          # Contar quantos termos foram
while cont <= 10:
    print('{} → '.format(primeiro), end=' ')
    primeiro += razao
    cont += 1
print('FIM.....')
