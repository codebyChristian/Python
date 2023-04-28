
# 036. Escreva um programa para aprovar o empréstimo bancário para a comprar
# de uma casa. O programa vai perguntar o valor da casa, o sálario
# do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do sálario ou então o empréstimo será negado.


casa = float(input('Olá, qual é o valor da casa desejada? R$'))
salario = float(input('Qual é seu salário para verificarmos: R$'))
ano = int(input('Você quer pagar em quantos anos?'))
novoano = ano * 12
casa1 = casa / novoano   # prestacao = casa / (ano * 12)
if casa1 >= salario * 31 / 100:
  print('Para pagar uma casa de R${:.2f} em {} anos a prestação séra de \033[36mR${:.2f}\033[m Reais'.format(casa, ano, casa1))
  print('Desculpe, mas o empréstimo foi negado.')
else:
   print('Parabéns você conseguio o empréstimo:')
   print('Você irá pagar por mês \033[36m{:.2f}\033[m Reais por mês!'.format(casa1))
