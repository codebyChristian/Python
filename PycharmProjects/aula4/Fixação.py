#Dada uma lista contendo as notas de alunos
#em uma disciplina, escreva uma expressão
#para:
#notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

#) Encontrar quantos alunos tiraram nota 7
nota = [9, 7, 7, 10, 3, 9, 6, 6, 2]

print('A nota 7 saiu:',nota.count(7))

#b) Alterar a última nota para 4
nota = [9, 7, 7, 10, 3, 9, 6, 6, 2]
nota[-1] = 4
print(nota[-1])

# Encontrar a maior nota


#) Ordenar a lista de notas
nota = [9, 7, 7, 10, 3, 9, 6, 6, 2]
nota.sort()

# A média das notas