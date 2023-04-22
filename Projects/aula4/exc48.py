# Calcule a soma entre todos os números ímpares que são múltiplos de três entre 1 até 500

impar = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            d = c
            impar += d
print('A soma de todos os ímpares múltiplos de três é \033[35m{}\033[m'.format(impar))

# ´----Versão professor----

soma = 0
cont = 0
for d in range(1, 501, 2):
    if d % 3 == 0:
        soma += d
        cont += 1
print('A soma de todos os \033[34m{}\033[m múltiplos de 3 é \033[31m{}\033[m'.format(cont, soma))

