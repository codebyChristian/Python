# AULA 09------------------------------------


frase = 'Curso em Vídeo Python'
print(frase[:13])
print(frase[13:])
print(frase[1:15:2])
print(frase[1::2])
print(frase[::2])
print("""Texte de texto longo com três aspás
#duplas digitando apenas um print:""")

print(frase.count('o'))  # Quantas letras 'o' tem:
print(frase.upper().count('O'))  #(upper coloca tudo para maiuscula:
print(len(frase))  # Tamanho da frase (espaço conta como caractere
print(len(frase.strip()))  # Remove espaços indesejados antes e depois da frase

print(frase.replace('Python', 'Android')) # Replace troca uma frase por outra:

frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')  # String é imutavel mas salvando pode trocar
print(frase)

print('Curso' in frase)  # True
print(frase.find('Curso'))  # Mostra o ínicio da palavra 'curso':

print(frase.lower().find('vídeo'))  # lower coloca a frase para minusculo


print(frase.split())  # colocar frase em uma lista separando

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0])  # Mostra o 1º conteudo da lista
print(dividido[2][3]) # Pega a 2ª palavra e mostra a letra 3(começa do zero)


