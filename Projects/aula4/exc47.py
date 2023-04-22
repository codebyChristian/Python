# Mostre na tela todos os números pares que estão entre 1 e 50

for c in range(1, 51):      # Muitas interações, assim o processador não aguenta
    if c % 2 == 0:
        print('\033[31m{}\033[m'.format(c), end=' ')  # Não pular linha
print('Acabou')

# ----versão professor------ Economiza processador
for d in range(2, 51, 2):
    print(d, end=' ')
