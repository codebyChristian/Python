# Um programa que leia uma frase qualquer e diga se ela é palíndromo, sem espaços
# apos a sopa
frase = str(input('Digite qualquer frase: > ')).strip().upper()   # tirar os espaços entre as palavras e transforma para maiuscula
palavras = frase.split()  # Separa todas as palavras que tenha espaços
junto = ''.join(palavras)  # Junta todas palavras com espaço
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('A frase é {} e o inverso é {}'.format(junto, inverso))
if inverso == junto:
    print('\033[35mÉ PALÍNDROMO\033[m...')
else:
    print('\033[31mNÃO É PALÍNDROMO\033[m...')


# MACETE
frase = str(input('Digite qualquer frase: > ')).strip().upper()   # tirar os espaços entre as palavras e transforma para maiuscula
palavras = frase.split()  # Separa todas as palavras que tenha espaços
junto = ''.join(palavras)  # Junta todas palavras com espaço
inverso = junto[::-1]  # doidera fatiamento
print('A frase é {} e o inverso é {}'.format(junto, inverso))
if inverso == junto:
    print('\033[35mÉ PALÍNDROMO\033[m...')
else:
    print('\033[31mNÃO É PALÍNDROMO\033[m...')
