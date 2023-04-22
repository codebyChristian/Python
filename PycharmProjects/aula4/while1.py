# Inteiros de 3 até 12, com 12 incluso
x = 3
while (x < 13):
    print(x)
    x = x + 1

# Inteiros de 0 até 9, excluindo o 9, com passo de 2
x = 0
while (x <9):
    print(x)
    x = x + 2


# pratica 4
print('CALCULADORA')
print('(+) SOMA')
print('(-) DIVISÃO')
print('(*) MULTIPLICAÇÃO')
print('(/) DIVISÃO)')

opera = input('Qual operação voçê quer fazer:')
if opera == '+' or opera == '-' or opera == '*' or opera == '/':
    x = int(input('Escreva o número:'))
    y = int(input('Escreva o número:'))

while (opera != 'sa'):
    if (opera == '+'):
        print('O resultado é {} :'.format(x + y))
    elif (opera == '-'):
        print('O resultado é {} :'.format(x - y))
    elif (opera == '/'):
        print('O resultado é {} :'.format(x / y))
    elif (opera == '*'):
        print('O resultado é {} :'.format(x * y))
    else:
        print('Invalido')

    opera = input('Qual operação voçê quer fazer:')
    if opera == '+' or opera == '-' or opera == '*' or opera == '/':
        x = int(input('Escreva o número:'))
        y = int(input('Escreva o número:'))

print('Encerado')