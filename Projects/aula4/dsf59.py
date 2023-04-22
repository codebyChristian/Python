# Leia dois valores e mostra um menu
# 1 somar 2 multiplicar 3 maior 4 novos números 5 sair
# Deverá realizar todas as operações
a = int(input('1º número > '))
b = int(input('2º número > '))
print('[ 1 ] SOMA \n'
      '[ 2 ] MULTIPLICAR\n'
      '[ 3 ] MAIOR \n'
      '[ 4 ] TROCAR OS NÚMEROS\n'
      '[ 5 ] SAIR')
print('*' * 20)
menu = 0
while menu != 5:
    print('[ 1 ] SOMA \n'
          '[ 2 ] MULTIPLICAR\n'
          '[ 3 ] MAIOR \n'
          '[ 4 ] TROCAR OS NÚMEROS\n'
          '[ 5 ] SAIR')
    menu = int(input('Didite a opção escolhida > '))
    if menu == 1:
        print('A soma de {} + {} será {}'.format(a, b, a+b))
    elif menu == 2:
        print('A multiplicação de {} * {} será {}'.format(a, b, a*b))
    elif menu == 3:
        if a > b:
            print('{} é maior de {}'.format(a, b))
        elif b > a:
            print('{} é maior de {}'.format(b, a))
        else:
            print('São números iguais')
    elif menu == 4:
        print('Escolha outros números. Novamente...')
        a = int(input('1º número > '))
        b = int(input('2º número > '))
    elif menu == 5:
        print('Finalizando...')

