#026: Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e
# em que posição ela aparece a última vez

frase = str(input('Escreva uma frase:')).strip()
print('A letra (A) aparece {} vezes na frase: '.format(frase.lower().count('a')))
print('Primeira vez foi na posição {}'.format(frase.lower().find('a') + 1))
print('A ultima vez foi na posição {}'.format(frase.lower().rfind('a') + 1))
