# Sorteando alunos aleatoriamentes

import random  # from random import choiche
aluno1 = str(input('Primeiro aluno:'))
aluno2 = str(input('Segundo aluno:'))
aluno3 = str(input('Terceiro aluno:'))
aluno4 = str(input('Quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(lista)
print('O aluno sorteado foi {} '.format(sorteado))
