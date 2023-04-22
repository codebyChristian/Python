somatoria = 0
a = 0
print('Seja bem-vindo a lanchonete Christian Ernany Cardoso Dos Santos')
print('-------------OPÇÕES DE PRODUTOS-----------------')
print('|CÓDIGO| |       DESCRIÇÃO       | | VALOR(R$) |')
print('| 100  | |    Cachorro-Quente    | |   9,00    |')
print('| 101  | | Cachorro-Quente Duplo | |   11,00   |')
print('| 102  | |         X-Egg         | |   12,00   |')
print('| 103  | |       X-Salada        | |   13,00   |')
print('| 104  | |        X-Bacon        | |   14,00   |')
print('| 105  | |        X-Tudo         | |   17,00   |')
print('| 200  | | Refrigerante de Lata  | |   5,00    |')
print('| 201  | |      Chá Gelado       | |   4,00    |')
while a == 0:
    codigo = input('Entre com o código do produto desejado: ')
    if codigo == '100':
        somatoria = somatoria + 9
    elif codigo == '101':
        somatoria = somatoria + 11
    elif codigo == '102':
        somatoria = somatoria + 12
    elif codigo == '103':
        somatoria = somatoria + 13
    elif codigo == '104':
        somatoria = somatoria + 14
    elif codigo == '105':
        somatoria = somatoria + 17
    elif codigo == '200':
        somatoria = somatoria + 5
    elif codigo == '201':
        somatoria = somatoria + 4
    else:
        print('Código invalida...Por favor tente novamente:')
        continue
    print('O valor a ser pago está em: {:.2f}'.format(somatoria))
    resposta = input('Deseja algo mais: (s/n) ')
    if resposta == 's':
        continue
    else:
        print('O valor final da conta é: {:.2f}'.format(somatoria))
        break