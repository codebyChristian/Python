
# 040. Leia duas notas de um aluno e calcule média,
# Média abaixo de 5 Reprovado
# Média entre 5 e 6.9 Recuperação
# Média superior a 7 Aprovado

print('Calculo de média...')
nota1 = float(input('Qual é sua Primeira nota?'))
nota2 = float(input('Qual é sua Segunda nota?'))
media = (nota1 + nota2) / 2
if media < 5:
   print('Com a nota {} e {}: Infelizzmente você foi reprovado com média \033[31m{:.1f}\033[m...'.format(nota1, nota2, media))
elif 7 > media >= 5:
   print('Com a nota {} e {}: Você ficou em recuperação com a média em \033[33m{:.1f}\033[m...'.format(nota1, nota2, media))
else:
  print('Com a nota {} e {}: Você foi aprovado com média \033[34m{:.1f}\033[m'.format(nota1, nota2, media))
