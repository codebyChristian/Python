# Tabuada do número que o úsuario escolher

i = 0
c = int(input('Digite qualquer número: E aparecerá a tabuada dele > '))
for i in range(0, 11, 1):
    i *= c
    print(' \033[31m{}\033[m '.format(i), end=' ')


# -----Versão professor----

num = int(input('Digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))

