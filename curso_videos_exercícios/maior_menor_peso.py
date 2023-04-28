# Leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {} pessoa > Kg '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é \033[31m{}Kg\033[m'.format(maior))
print('O menor peso é \033[36m{}Kg\033[m'.format(menor))

