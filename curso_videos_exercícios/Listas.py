#Escreva um algoritmo em Python que crie uma lista vazia e vá adicionando valores referentes às
#notas de um aluno nesta lista. Quando o usuário desejar parar de digitar notas (digitando um valor
#negativo, por exemplo), calcule a média das notas digitadas.

try:
    notas = []
    x = float(input('Digite a nota:'))
    while x >= 0:
        notas.append(x)
        x = float(input('Digite a nota:'))
    soma = 0
    for i in notas:
        soma += i
    media = soma/len(notas)
    print(notas)
    print('Médias das notas {}'.format(media))
except ZeroDivisionError:
    print('Valor digitado é invalido. Encerrando')




