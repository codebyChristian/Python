

# Faça um programa que leia três números e mostre
# qual é o maior e qual é o menor.

a = int(input('Digite qualquer número:'))
b = int(input('Digite qualquer número:'))
c = int(input('Digite qualquer número:'))
num = [a, b, c]
print('O menor número digitado foi {}:'.format(min(num)))
print('O maior número digitado foi {}:'.format(max(num)))  



# Versão do diferente------------

a = int(input('Digite o PRIMEIRO número:'))
b = int(input('Digite o SEGUNDO número:'))
c = int(input('Digite o TERCEIRO número:'))
## Verificar quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor valor é {}'.format(menor))
# Verificar quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor é {}'.format(maior))
