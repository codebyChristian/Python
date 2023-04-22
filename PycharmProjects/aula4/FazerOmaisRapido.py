#Crie um programa para ler o nome, ano de  nascimento e sexo de diferentes pessoas
#Armazene os dados em um dicionário com listas Ao encerrar o cadastro, apresente:
#O total de cadastros efetuados A média das idades das pessoas
#Uma lista de mulheres com menos de 30 anos Uma lista de homens com idade acima da média


cadastro = {'nome': [], 'sexo': [], 'ano': []}
total = 0
while True:
    terminar = input('Deseja cadastra uma pessoa? (S / N)>')
    if terminar.upper() in 'N':   # Pega o n é passa para maiusculo
        break
    if terminar.upper() not in 'S':
        print('Digite S para SIM ou N para NÂO:')
        continue
    nome = input('Qual seu nome? ')
    sexo = input('Qual seu seu sexo (M / F)> ')
    ano = int(input('Qual seu ano de nascimento? '))
    idade = 2020 - ano
    media = idade / 2
    total += 1
    cadastro['nome'].append(nome)
    cadastro['sexo'].append(sexo.upper())
    cadastro['ano'].append(ano)
print(cadastro)
#O total de cadastros efetuados
print('O total de cadastro é: {}'.format(total))
#A média das idades das pessoas

