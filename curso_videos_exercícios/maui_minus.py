#022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
#  - Quantas letras tem o primeiro nome.

nome = str(input('Escreva seu nome completo:')).strip()
print('Seu nome em letras maiúsculas é {}:'.format(nome.upper()))
print('Seu nome em letras minúsculas é {}:'.format(nome.lower()))
print('Seu completo tem {} letras'.format(len(nome)-nome.count(' ')))
separado = nome.split()
print('Seu 1º nome é {} e tem {} letras!'.format(separado[0], len(separado[0])))

print('Seu 1º nome tem {} letras'.format(nome.find(' ')))
