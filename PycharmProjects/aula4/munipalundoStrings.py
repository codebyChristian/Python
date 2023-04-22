#print('Olá funcionário:')
#salario = float(input('Qual é o seu sálario? R$'))
#aumento = float(int(input('Qual é a porcentagem de aumento?')))
#novo = (salario * aumento) / 100 + salario
#print('O seu salário era {:.2f}R$: com o aumento de {}% ficou {:.2f}R$'.format(salario,aumento,novo))

#print('TEMPERATURA')
#temp = float(input('Qual a temperatura em ºC:'))
#f = 9 * temp / 5 + 32
#print('A temperatura em {}ºC corresponde {}ºF!'.format(temp,f))


#print('Aluguel de Carros')
#kilo = float(int(input('Quantos Quilômetros perroridos:>')))
#dias = int(input('Quantos dias de uso:>'))
#preco = 60 * dias + 0.15 * kilo
#print('Você rodou {}Km, e usou o carro em {}dia(s): Então o preço será R${:.2f}'.format(kilo,dias,preco))

#import math
#num = int(input('Digite um número:'))
#raiz = math.sqrt(num)                                              # math.floor(raiz))) Arrendonda para baixo
#print('A raiz de {} é igual {}'.format(num, math.ceil(raiz)))     # math.ceil(raiz))) Arredonda a raiz para cima


#from math import sqrt   # Adicionar , e outra função
#num = int(input('Digite um número:'))
#raiz = sqrt(num)                                              # math.floor(raiz))) Arrendonda para baixo
#print('A raiz de {} é igual {}'.format(num, raiz))     # math.ceil(raiz))) Arredonda a raiz para cima


#import random                 # Números aleatorios
#num = random.randint(1, 10)   # De 1 até 10
#print(num)

#import emoji
#print(emoji.emojize("Olá, Mundo :globe_showing_Americas:", use_aliases=True))


# Crei um programa que leia um número real e mostre na tela sua parte inteira  (Importando)
#from  math import trunc
#nume = float(input('Digite um número Real: '))
#print('O valor digitado foi {}: e a parte inteira é {}'.format(nume, trunc(nume)))
# (Sem importação)
#num = float(input('Digite um número real:'))
#print('O valor digitado foi {}: a parte inteira é {}:'.format(num, int(num)))


# Leia o comprimento do cateto oposto e o cateto adjacente, e calcule a hipotenusa
#from math import hypot
#oposto = float(input('Digite o cateto oposto do triângulo:'))
#adja = float(input('Digite o cateto adjacente do triângulo:'))
#print('O cateto oposto é {}, e cateto adjacente é {}: Então a hipotenusa será {:.2f}'.format(oposto, adja, hypot(oposto, adja) ))

# Sem importação
#co = float(input('Digite o comprimento do cateto oposto:'))
#ca = float(input('Digite o comprimento do cateto adjacente:'))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir: {:.2f}'.format(hi))

# Qual seno e cosseno
#import math  (from math import radians, sin, cos, tan
#num = float(input('Digite o ângulo logo:'))
#seno = math.sin(math.radians(num))
#print('O ângulo de {} tem SENO de {:.2f} '.format(num, seno))
#cosseno = math.cos(math.radians(num))
#print('O ângulo de {} tem COSSENO de {:.2f} '.format(num, cosseno))
#tangente = math.tan(math.radians(num))
#print('A ângulo de {} tem TANGENTE de {:.2f} '.format(num, tangente))


# Sorteando alunos aleatoriamentes
#import random  # from random import choiche
#aluno1 = str(input('Primeiro aluno:'))
#aluno2 = str(input('Segundo aluno:'))
#aluno3 = str(input('Terceiro aluno:'))
#aluno4 = str(input('Quarto aluno:'))
#lista = [aluno1, aluno2, aluno3, aluno4]
#sorteado = random.choice(lista)
#print('O aluno sorteado foi {} '.format(sorteado))

# Ordem de apresentação de trabalho
#import random #(from random import shuffle
#aluno1 = str(input('Primeiro aluno '))   # str não é obrigatorio
#aluno2 = str(input('Segundo aluno '))
#aluno3 = str(input('Terceiro aluno '))
#aluno4 = str(input('Quarto aluno '))
#lista = [aluno1, aluno2, aluno3, aluno4]
#random.shuffle(lista)
#print('A ordem de apresentação será')
#print(lista)

# TOCANDO MÚSICA NO PYTHON
#import pygame

#pygame.init()
#pygame.mixer.music.load('ex021.mp3')
#pygame.mixer.music.play()
#input()
#pygame.event.wait()

# AULA 09------------------------------------
#frase = 'Curso em Vídeo Python'
#print(frase[:13])
#print(frase[13:])
#print(frase[1:15:2])
#print(frase[1::2])
#print(frase[::2])
#print("""Texte de texto longo com três aspás
#duplas digitando apenas um print:""")

#print(frase.count('o'))  # Quantas letras 'o' tem:
#print(frase.upper().count('O'))  #(upper coloca tudo para maiuscula:
#print(len(frase))  # Tamanho da frase (espaço conta como caractere
#print(len(frase.strip()))  # Remove espaços indesejados antes e depois da frase

#print(frase.replace('Python', 'Android')) # Replace troca uma frase por outra:

#frase = 'Curso em Vídeo Python'
#frase = frase.replace('Python', 'Android')  # String é imutavel mas salvando pode trocar
#print(frase)

#print('Curso' in frase)  # True
#print(frase.find('Curso'))  # Mostra o ínicio da palavra 'curso':

#print(frase.lower().find('vídeo'))  # lower coloca a frase para minusculo


#print(frase.split())  # colocar frase em uma lista separando

#frase = 'Curso em Vídeo Python'
#dividido = frase.split()
#print(dividido[0])  # Mostra o 1º conteudo da lista
#print(dividido[2][3]) # Pega a 2ª palavra e mostra a letra 3(começa do zero)



#022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
#  - Quantas letras tem o primeiro nome.
#nome = str(input('Escreva seu nome completo:')).strip()
#print('Seu nome em letras maiúsculas é {}:'.format(nome.upper()))
#print('Seu nome em letras minúsculas é {}:'.format(nome.lower()))
#print('Seu completo tem {} letras'.format(len(nome)-nome.count(' ')))
#separado = nome.split()
#print('Seu 1º nome é {} e tem {} letras!'.format(separado[0], len(separado[0])))

#print('Seu 1º nome tem {} letras'.format(nome.find(' ')))


#023: Faça um programa que leia um número de 0 a 9999 ,e
# mostre na tela cada um dos dígitos separados

#num = int(input('Informe um número:'))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('Analisando o número {}'.format(num))
#print('Unidade {}'.format(u))
#print('Dezena {}'.format(d))
#print('Centena {}'.format(c))
#print('Milhar {}'.format(m))

#024: Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome "SANTO".
#cidade = str(input('Digite o nome de uma cidade:')).strip()  # EU
#fatia = cidade.strip()
#print(fatia[0].upper() in 'SANTO')

#city = input('Nome da cidade:').strip()  # elimina espaços indejejados
#print(city[:5].upper() == 'SANTO')   # PROFER

#025: Crie um programa que leia o nome de uma pessoa e
# diga se ela tem "SILVA" no nome.
#pessoa = str(input('Escreva um nome:')).strip()  # EU
#print('SILVA' in pessoa.upper())

#nome = input('Qual seu nome:')
#print('seu nome tem Silva? {}'.format('silva' in nome.lower()))

#026: Faça um programa que leia uma frase pelo teclado e
# mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e
# em que posição ela aparece a última vez
#frase = str(input('Escreva uma frase:')).strip()
#print('A letra (A) aparece {} vezes na frase: '.format(frase.lower().count('a')))
#print('Primeira vez foi na posição {}'.format(frase.lower().find('a') + 1))
#print('A ultima vez foi na posição {}'.format(frase.lower().rfind('a') + 1))


#027: Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
#completo = str(input('Nome completo:')).strip()
#nome = completo.split()
#print('Prazer em conhecer!')
#print('Seu Primeiro nome é {}'.format(nome[0]))
#print('Seu último nome é {}'.format(nome[len(nome)-1]))  # O -1 é o último objeto de uma lista como -2 seria a penultima


