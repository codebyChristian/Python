n = 1            # Uma variavel de controle
par = impar = 0  # Pode forma duas variaveis de controle juntas
while n != 0:    # Quando não for digitado 0 não para
    n = int(input('Digite qualquer valor: '))
    if n != 0:   # Para não contar o 0 como par
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou \033[33m{}\033[m Nº pares e \033[35m{}\033[m Nº impares'.format(par, impar))

