#nome = str(input('Qual seu nome? '))
#if nome == 'Chris':
#    print('Nome estopendo:')
#else:
#    print('Nice to meet you!')
#print('Bom dia, {}!'.format(nome))


#nota1 = float(input('Qual sua primeira nota: '))
#nota2 = float(input('Qual sua segunda nota: '))
#media = (nota1 + nota2) / 2
#print('Sua média é {:.1f}'.format(media))
#print('Parabens' if media >=6 else 'Reprovado!')   # Forma simples mas confusa
#if media >= 7:
#    print('Parabens, você foi aprovado!')
#else:
#    print('Se lascou foi Reprovado:')

# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usúario venceu ou perdeu
#import random
#advin = int(input('Tente advinhar um número de 1 a 5>> '))
#pensar = random.randint(1, 5)
#print('O número sorteado foi {}:'.format(pensar))
#if advin == pensar:
#    print('Parabens você é um cagão')
#else:
#    print('È você errou!')

# ----VERSÃO DO PROFESSOR-----
#from random import randint
#from time import sleep        # Essa simular processamento
#computador = randint(0, 5)
#print('-=-' * 20)
#print('Vou pensar em um número entre 0 e 5. Tente adinvinhar...')
#print('-=-' * 20)
#jogador = int(input('Qual número estou pensando? '))
#print('PROCESSANDO....')
#sleep(2)   # Espera 2 segundos para mostrar a resultados
#if jogador == computador:
  #  print('PARABENS! Você acertou:')
#else:
#    print('GANHEI! Eu pensei no número {} e não {}.'.format(computador, jogador))




# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00
# por cada Km acima do limite.

#veloz = float(input('A velocidade do carro é > '))
#if veloz > 80:
 #   print('Você está sendo multado...'
 #         'Você excedeu o limite de 80Km/h'
 #         'Você irá pagar uma multa!')
#    nume = veloz - 80    # multa = (veloz - 80) * 7 Támbem serve
#    print('O valor da multa é {:.2f} Reais:'.format(nume * 7))
#else:                # Não precisa usar else é facultativo
 #   print('Um bom dia e dirija com segurança::')


#Crie um programa que leia um número inteiro
# e mostre na tela se ele é PAR ou ÍMPAR.

#nume = int(input('Digite qualquer número >'))
#if nume % 2 == 0:     # % é resto de devisão
#    print('O número {} é PAR'.format(nume))   # Resto de divisão é 0
#else:
 #   print('O número {} é ÍMPAR'.format(nume))  # Resto de divisão é 1


# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule e peça o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R#0,45
# para viagens mais longas

#distan = float(input('Qual a distância de sua viagem > '))
#if distan <= 200:
 #   valor = distan * 0.50
 #   print('O valor a ser pago em é {:.2f} Reais'.format(valor))
#else:
#    conta = distan * 0.45
#    print('O valor a ser pago em é {:.2f} Reais'.format(conta))

# -------------SIMPLIFICADA------------
#distan = float(input('Qual a distância de sua viagem > '))
#preco = distan * 0.50 if distan <= 200 else distan * 0.45
#print('E o preço de sua passagem será RS{:.2f}'.format(preco))


# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

#from datetime import date
#ano = int(input('Digite qualquer ano >  Coloque 0 para analisar o ano atual:'))
#if ano == 0:
 #   ano = date.today().year   # Pegar o ano atual da máquina
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # È divisivel por 4 exceto por 100 e 400
 #   print('O ano {} é BISSEXTO:'.format(ano))
#else:
 #   print('O ano {} NÃO É BISSEXTO'.format(ano))


# Faça um programa que leia três números e mostre
# qual é o maior e qual é o menor.

#a = int(input('Digite qualquer número:'))
#b = int(input('Digite qualquer número:'))
#c = int(input('Digite qualquer número:'))
#num = [a, b, c]
#print('O menor número digitado foi {}:'.format(min(num)))
#print('O maior número digitado foi {}:'.format(max(num)))    -----------------------------------


# Versão do professor------------

#a = int(input('Digite o PRIMEIRO número:'))
#b = int(input('Digite o SEGUNDO número:'))
#c = int(input('Digite o TERCEIRO número:'))
## Verificar quem é menor
#menor = a
#if b < a and b < c:
#    menor = b
#if c < a and c < b:
 #   menor = c
#print('O menor valor é {}'.format(menor))
# Verificar quem é o maior
#maior = a
#if b > a and b > c:
#    maior = b
#if c > a and c > b:
 #   maior = c
#print('O maior valor é {}'.format(maior))



# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a R$1.250,00, calcule
# um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.

#salario = float(input('Seu salário em REAIS: R$ '))
#if salario >= 1.250:       # ERRADO
#    novo = (salario * 0.10) + salario
#    print('Com o aumento você deixou de receber {:.2f} e agora vai ganhar {:.2f} Reais'.format(salario, novo))
#else:
 #   nov = (salario * 0.15) + salario
  #  print('Com o aumento você deixou de receber {:.2f} e agora vai ganhar {:.2f} Reais'.format(salario, nov))

# versão do professor
#salario = float(input('Qual é o seu salário em REAIS: R$'))
#if salario <= 1250:
#    novo = salario + (salario * 15 / 100)
#else:
#    novo = salario + (salario * 10 / 100)
#print('Você ganhava {:.2f} agora vai receber {:.2f}:'.format(salario, novo))

#Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

#reta1 = float(input('Qual o comprimento da reta 1: '))
#reta2 = float(input('Qual o comprimento da reta 2: '))             # CERTA
#reta3 = float(input('Qual o comprimento da reta 3: '))
#if reta1 > 0 and reta2 > 0 and reta3 > 0:  # Se alguma reta for igual a 0 não é possível forma um triangulo.
#    if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
 #       print('Existe esse triângulo.')
 #   else:
  #      print('Não existe este triângulo com essas medidas:')
#else:
 #   print('Não existe triângulo com reta 0.')

# -=-=-=-=-=-=-=-VERSÃO DO PROFESSOR-=-=-=-=-=-=-=

#print('ANALISADOR DE TRIÂNGULOS')
#r1 = float(input('Primeiro segmento:'))
#r2 = float(input('Segundo segmento:'))
#r3 = float(input('Terceiro segmento:'))    # Se uma reta for menor que a soma das outros duas retas não forma um triângulo
#if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#    print('Os segmentos acima formam um Triângulo:')
#else:
 #   print('Esses segmentos não formam um Triângulo:')

