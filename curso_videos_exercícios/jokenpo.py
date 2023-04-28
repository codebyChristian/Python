
# Crie um jogo Jokenpô que o computador joque comigo:
# Pedra, Papel, Tesoura   # importa random

from random import randint
from time import sleep
print('JOGUE COMIGO...')
print('...JOKENPÔ...')
print('OLHE Á TABELA\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA\n')
itens = ('Pedra', 'Papel', 'Tesoura')
jogada = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)
computer = randint(0, 2)
print('*' * 25)
print('\033[35mComputador jogou {}\033[m'.format(itens[computer]))
print('\033[31mVocê jogou {}\033[m'.format(itens[jogada]))
print('*' * 25)
if jogada == 0:
    if computer == 0:
        print('Ocorreu um empate:')
    elif computer == 1:
        print('\033[31mComputador vence\033[m:')
    elif computer == 2:
        print('\033[34mVocê venceu\033[m:')
    else:
        print('JOGADA ÍNVALIDA')
elif jogada == 1:
    if computer == 0:
        print('\033[34mVocê venceu\033[m:')
    elif computer == 1:
        print('Ocorreu um empate:')
    elif computer == 2:
        print('\033[31mComputador vence\033[m:')
    else:
        print('JOGADA ÍNVALIDA')
elif jogada == 2:
    if computer == 0:
        print('\033[31mComputador vence\033[m:')
    elif computer == 1:
        print('\033[34mVocê venceu\033[m:')
    elif computer == 2:
        print('Ocorreu um empate:')
    else:
        print('JOGADA ÍNVALIDA')
else:
    print('Número inválido...')

