# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usúario venceu ou perdeu

import random
advin = int(input('Tente advinhar um número de 1 a 5>> '))
pensar = random.randint(1, 5)
print('O número sorteado foi {}:'.format(pensar))
if advin == pensar:
    print('Parabens você é um cagão')
else:
    print('É você errou!')

# ----VERSÃO MAIS ARRUMADA-----
from random import randint
from time import sleep        # Essa simular processamento
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adinvinhar...')
print('-=-' * 20)
jogador = int(input('Qual número estou pensando? '))
print('PROCESSANDO....')
sleep(2)   # Espera 2 segundos para mostrar a resultados
if jogador == computador:
    print('PARABENS! Você acertou:')
else:
    print('GANHEI! Eu pensei no número {} e não {}.'.format(computador, jogador))