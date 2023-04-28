print('CALCULADORA')
print('+')
print('-')
print('*')
print('/')
opera = input('Qual operação voçê quer fazer:')
x = int(input('Escreva o número:'))
y = int(input('Escreva o número:'))
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
print('Encerado')