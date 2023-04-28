# Leia o nome, idade, sexo de quatro pessoas.
# Mostre média de idade do grupo
# Qual o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos
# Vai ter manipulaçao de string

from datetime import date
atual = date.today().year
maior = 0   # Conta quantas mulheres é abaixo da idade pedida
media = 0   # Separa todas idades
cont = 0    # Junta as idades e soma
homem = 0   # Homem mais velho
nomevelho = 0  # nome
for c in range(1, 5):
    nome = str(input('Qual o NOME {}* pessoa > '.format(c))).strip()
    nasc = int(input('Qual o ANO DE NASCIMENTO da {}* pessoa > '.format(c)))
    sexo = str(input('Qual é o SEXO da {}* pessoa: M / F > '.format(c))).strip().upper()
    man = nome.split()  # Separa todas as palavras que tenha espaços
    junto = ' '.join(man)  # Junta todas palavras com espaço
    idade = atual - nasc
    cont += 1                                                   # Soma uma idade ao contador
    media += idade                                           # Pega todas as idades e soma
    if sexo == 'F':
        if idade < 20:
            maior += 1
    if c == 1 and sexo == 'M':
        homem = nome
        nomevelho = nome
    if sexo == 'm' and idade > homem:
        homem = idade
        nomevelho = nome

print('Tem \033[33m{}\033[m mulheres com menos de 20 anos'.format(maior))
print('A média de idade do grupo é de \033[34m{:.0f}\033[m'.format(media/4))
print('A idade do homem mais velho do grupo é \033[35m{}\033[m anos'.format(homem))
print('O nome do homem mais velho é \033[31m{}\033[m'.format(nomevelho))

