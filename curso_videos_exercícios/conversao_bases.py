# 037. Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão
# 1- para binário
# 2- para octal
# 3- para hexadecimal


print('Bem-vindo ao convertor de unidades.')
numero = int(input('Digite qualquer número:'))
opcao = int(input('Digite uma opção para converter.\n'
                  '1 - Binário\n'
                  '2 - Octal\n'
                  '3 - Hexadecimal\n'
                  'Escolhar a base da conversão:\n'))
if opcao == 1:
    print('{} convertido para BÍNARIO é igual a {} '.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {} '.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Número inválido:')