# ----------CONDIÇÕES ANINHADAS------------

# -------------------------------------------------------------------------
# nome = str(input('Qual é seu nome? '))
# if nome == 'Chris':
#    print('Que nome bonito!')
# elif nome == 'João' or nome == 'Maria' or nome == 'Jose' or nome == 'Jobescleiton':
#    print('Esse nome é bastante popular!')
# elif nome in 'Ana Claudia Jéssica Juliana':
#    print('Belo nome feminino!')
# else:
#    print('Este nome é bem louco!')
# print('Tenha um Bom Dia, {}'.format(nome))
# --------------------------------------------------------------------

# 036. Escreva um programa para aprovar o empréstimo bancário para a comprar
# de uma casa. O programa vai perguntar o valor da casa, o sálario
# do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do sálario ou então o empréstimo será negado.


# casa = float(input('Olá, qual é o valor da casa desejada? R$'))
# salario = float(input('Qual é seu salário para verificarmos: R$'))
# ano = int(input('Você quer pagar em quantos anos?'))
# novoano = ano * 12
# casa1 = casa / novoano   # prestacao = casa / (ano * 12)
# if casa1 >= salario * 31 / 100:
#   print('Para pagar uma casa de R${:.2f} em {} anos a prestação séra de \033[36mR${:.2f}\033[m Reais'.format(casa, ano, casa1))
#   print('Desculpe, mas o empréstimo foi negado.')
# else:
#    print('Parabéns você conseguio o empréstimo:')
#   print('Você irá pagar por mês \033[36m{:.2f}\033[m Reais por mês!'.format(casa1))


# 037. Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão
# 1- para binário
# 2- para octal
# 3- para hexadecimal


print('Bem-vindo ao convertor de unidades.')
numero = int(input('Digite qualquer número:'))
opcao = int(input('Digite uma opção para converter.\n'
                  '1 - Binário\n'
                  '2 - Octal\n'
                  '3 - Hexadecimal\n'
                  'Escolhar a base da conversão:\n'))
if opcao == 1:
    print('{} convertido para BÍNARIO é igual a {} '.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {} '.format(numero, oct(numero)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Número inválido:')


# 038. Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem
# O primeiro valor é maior
# O segundo valor é menor
# Não existe valor maior, os dois são iguais


# print('Irei dizer qual é o maior e o menor!')
# a = int(input('Digite um número inteiro:'))
# b = int(input('Digite outro número inteiro:'))
# if a > b:
#    print('O Primeiro valor \033[31m{}\033[m é maior e o Segundo valor \033[34m{}\033[m é menor:'.format(a, b))
# elif a < b:
#    print('O Segundo valor \033[34m{}\033[m é maior e o Primeiro valor \033[31m{}\033[m é menor:'.format(b, a))
# else:
#    print('Os dois valores \033[35m{}\033[m e \033[35m{}\033[m são iguais...'.format(a, b))

# 039. Que leia o ano de nascimento de um jovem e informe, de acordo com idade
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Deverá mostrar o tempo que falta ou que passou do prazo
# Use o ano do sistema


# print('Bem-vindo ao verificador do alistamento militar:')
# ano = int(input('Digite seu ano de nascimento:'))
# ano1 = 2022 - ano
# print('Você tem {} anos'.format(ano1))
# if ano1 >= 18:
#    print('Você ainda não se alistou no serviço militar:')
#    print('Já se passou \033[31m{}\033[m anos do alistamento:'.format(ano1 - 18))
# else:
#    print('Ainda não chegou sua vez:')
#   print('Mas falta \033[34m{}\033[m anos para o alistamento:'.format(18 - ano1))

# ----------------------------------------


# from datetime import date
# atual = date.today().year   # tem que criar uma varialvel
# nasc = int(input('Ano de nascimento:'))
# idade = atual - nasc
# print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
# if idade == 18:
#    print('Você tem que se alista IMEDIATAMENTE:')
# elif idade < 18:
#    saldo = 18 - idade
#    print('Você ainda não tem 18 anos. Ainda falta {} para o alistamento'.format(saldo))
#    ano = atual + saldo
#    print('Seu alistamento séra em {}'.format(ano))
# elif idade > 18:   # pode usar o else
#    saldo = idade - 18
#    print('Você já deveria ter se alistado há {} anos'.format(saldo))
#    ano = atual - saldo
#    print('Seu alistamento foi em {}'.format(ano))


# 040. Leia duas notas de um aluno e calcule média,
# Média abaixo de 5 Reprovado
# Média entre 5 e 6.9 Recuperação
# Média superior a 7 Aprovado

# print('Calculo de média...')
# nota1 = float(input('Qual é sua Primeira nota?'))
# nota2 = float(input('Qual é sua Segunda nota?'))
# media = (nota1 + nota2) / 2
# if media < 5:
#    print('Com a nota {} e {}: Infelizzmente você foi reprovado com média \033[31m{:.1f}\033[m...'.format(nota1, nota2, media))
# elif 7 > media >= 5:
#    print('Com a nota {} e {}: Você ficou em recuperação com a média em \033[33m{:.1f}\033[m...'.format(nota1, nota2, media))
# else:
#   print('Com a nota {} e {}: Você foi aprovado com média \033[34m{:.1f}\033[m'.format(nota1, nota2, media))


# Faça um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MÍRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 20 anos: SÊNIOR
# Acima: MASTER

# from datetime import date
# print('CLUBE DE NATAÇÃO')
# atual = date.today().year
# ano = int(input('Qual é o ano de nascimento:'))
# idade = atual - ano
# print('Você tem {} anos.'.format(idade))
# if idade <= 9:
#    print('Categoria: \033[33mMIRIM\033[m')
# elif idade <= 14:
#    print('Categoria: \033[34mINFANTIL\033[m')
# elif idade <= 19:
#    print('Categoria: \033[35mJUNIOR\033[m')
# elif idade <= 25:
#    print('Categoria: \033[36mSÊNIOR\033[m')
# elif idade > 25:
#    print('Categoria: \033[37mMASTER\033[m')

# Refaça desafio 35 do triângulo, dizendo como será ele
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

# print('Descubrindo os TRIÂNGULO:')
# reta1 = float(input('Digite a Primeira reta do triângulo: '))
# reta2 = float(input('Digite a Segunda reta do triângulo: '))
# reta3 = float(input('Digite a Terceira reta do triângulo: '))
# print('O triângulo com retas {:.0f}, {:.0f}, {:.0f}'.format(reta1, reta2, reta3))
# if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
#    print('Ele pode forma um TRIÂNGULO:', end=' ')
#    if reta1 == reta2 == reta3:
#        print('Esse Triângulo é \033[32mEQUILÁTERO\033[m')
#    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
#        print('Esse Triângulo é \033[33mISÓSCELES\033[m')
#    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
#        print('Esse Triângulo é \033[34mESCALENO\033[m')
#    else:
#        print('ASSISTA SOUTH PARK:')
# else:
#    print('\033[35mNão é possivel forma um TRIÂNGULO\033[m:')

# Calcule o IMC: peso / (altura * altura)
# Abaixo do peso: 18.5
# Peso ideal: entre 18.5 e 25
# Sobrepeso: 25 até 30
# Obesidade: 30 até 40
# Obesidade mórbida: acima 40

#print('DESCUBRAR SEU IMC')
#print('PRECISAREMOS DO SEU PESO E ALTURA')
#peso = float(input('Digite seu peso: (Kg)'))
#altura = float(input('Digite sua altura:'))
#Imc = peso / (altura * altura)  # Altura ao quadrado
#print('Você tem IMC de \033[35m{:.2f}\033[m'.format(Imc))
#if Imc < 18.5:
#    print('ALERTA: \033[31mVocê está ABAIXO DO PESO\033[m')
#elif 18.5 <= Imc <= 25:
#    print('Esse é o \033[32mPESO IDEAL\033[m')
#elif 25 <= Imc <= 30:
#    print('Você está com \033[33mSOBREPESO\033[m')
#elif 30 <= Imc <= 40:
#    print('Você está com \033[34mOBSIDADE\033[m')
#else:
 #   print('CUIDADO: Você está com \033[35mOBESIDADE MÓRBIDA\033[m')

# Leia o preço de um produto e mostre as condições de pagamenrtos
# Á vista dinheiro/cheque: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço normal
# 3x ou mais no cartão: 20% de juras

#print('VEJA AS CONDIÇÕES DE PAGAMENTOS\n'
#      'DIGITE O NÚMERO CORRESPONTENTE....\n'
#      '1: PARA PAGAMENTOS Á VISTA EM DINHEIRO OU CHEQUE: 10% DE DESCONTO\n'
#      '2: PARA PAGEMENTOS Á VISTA NO CARTÃO: 5% DE DESCONTO\n'
#      '3: PARA PAGAMENTOS EM ATÉ 2 VEZES: PREÇO NORMAL\n'
#      '4: PARA PAGAMENTOS ACIMA DE 3 VEZES: 20% DE JUROS\n')
#produto = float(input('Qual é valor do produto? R$'))
#numero = int(input('Qual a condição desejada: '))
#desconto1 = produto - (produto * 0.10)   # 10% de desonto
#desconto2 = produto - (produto * 0.05)   # 5% de desconto
#if numero == 1:
 #   print('Parabéns! O valor deixou de ser de {:.2f}R$ para \033[31m{:.2f}R$\033[m'.format(produto, desconto1))
#elif numero == 2:
#    print('Parabéns! O valor deixou de ser de {:.2f}R$ para \033[32m{:.2f}R$\033[m'.format(produto, desconto2))
#elif numero == 3:
#    total = produto
#    parcela = total / 2
#    print('O valor será 2x de R$\033[33m{:.2f}\033[m '.format(parcela))
#elif numero == 4:
#    meses = int(input('Em quantas vezes você irá pagar? '))
#    juros = produto + (produto * 0.20)
 #   parcela = juros / meses
#    print('Sua compra será parcelada em {}x de {:.2f} no final.'.format(meses, parcela))
#else:
#    print('\033[35mNÚMERO INVALIDO...\033[m')


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
