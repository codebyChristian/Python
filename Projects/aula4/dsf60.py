# Leia um número qualquer e mostre o fatorial dele

# Versão 1
# from math import factorial
# n = int(input('Digite um némero para calcular o fatorial: '))
# f = factorial(n)
# print('O fatorial de {}! é {}'.format(n, f))

# Versão 2

n = int(input('Digite um némero para calcular o fatorial: '))
c = n  # c começa por n
f = 1  # Multiplicação começa por 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))


# Criar outra versão com for
print("FATORIAL")
numero = int(input("Digite um número inteiro: "))
calculo = numero
fatorial = 1

