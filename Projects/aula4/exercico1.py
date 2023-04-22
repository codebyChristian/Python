#Escreva um algoritmo que crie uma tupla com
#10 palavras. Encontre dentro dessa tupla as
#vogais de cada palavra. Faça um print na tela
#com o nome da palavra e suas respectivas
#vogais
palavras = ['Mario', 'Chris', 'Ernany', 'Nintendo',
            'Androido', 'Meliodas', 'Levi'
            , 'Mikasa', 'Armi', 'Dedo Duro']

for palavra in palavras:
    print('\nPalavras: {}. Vogais: '.format(palavra.upper()), end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')