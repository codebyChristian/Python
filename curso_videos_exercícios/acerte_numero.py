# Tentar acerta o Nº de 0 a 10 do computador
# Tem que tentar até conseguir, e mostra quantos palpites foram precisos

from random import randint
vezes = 0
p = 1
while p:
    vezes += 1
    p = int(input('Tente acerta o número entre 0 e 10: '))
    computer = randint(1, 10)
    print('\033[34mVOCÊ jogou {}\033[m e o \033[35mROBO {}\033[m'.format(p, computer))
    if p == computer:
        print('\033[31mParabens\033[m')
        print('Você tentou \033[32m{}\033[m vezes'.format(vezes))
        break

# Versão professor

from random import randint
computer = randint(0, 10)
print('Ola sou um robo... Acabeu de pensar em um número entre 0 e 10.')
print('Será que você consegue acerta?')
acertou = False
palpites = 0
while not acertou:   # Enquanto não acerta ele não para.
    jogador = int(input('Qual seu palpite?'))
    palpites += 1
    if jogador == computer:
        acertou = True
    else:
        if jogador < computer:
            print('Mais...')
        elif jogador > computer:
            print('Menos...')
print('Acertou com {} palpites'.format(palpites))




