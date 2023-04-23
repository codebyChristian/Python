
# 038. Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem
# O primeiro valor é maior
# O segundo valor é menor
# Não existe valor maior, os dois são iguais


print('Irei dizer qual é o maior e o menor!')
a = int(input('Digite um número inteiro:'))
b = int(input('Digite outro número inteiro:'))
if a > b:
   print('O Primeiro valor \033[31m{}\033[m é maior e o Segundo valor \033[34m{}\033[m é menor:'.format(a, b))
elif a < b:
   print('O Segundo valor \033[34m{}\033[m é maior e o Primeiro valor \033[31m{}\033[m é menor:'.format(b, a))
else:
   print('Os dois valores \033[35m{}\033[m e \033[35m{}\033[m são iguais...'.format(a, b))
