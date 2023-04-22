#Escreva um algoritmo que permita cadastrar esses jogos informando o
#nome e a qual videogame ele pertence. Para isso, crie um menu de opções contendo:
#cadastrar novo item, listar tudo que foi cadastrado e sair.
#Para resolver esse exercício, crie pelo menos uma função para cada item do menu.
#Além disso, armazene todos os dados em um arquivo de texto que deve ser salvo em disco e manter os dados cadastrados


def valida_int(pergunta, min, max): # Valida uma função
  x = int(input(pergunta))
  while ((x < min) or (x > max)):
    x = int(input(pergunta))
  return x
#Função de criar arquivo
def criaArquivo(nomeArquivo):  # O nome arquivo poderia ser diferente
  try:
    a = open(nomeArquivo, 'wt+') # escrita , texto , criação
    a.close()
  except:
    print('Erro na criação do arquivo')
  else:
    print('Arquivo {} foi criado com sucesso!\n'.format(nomeArquivo))

#Função de procurar se o arquivo existe
def existeArquivo(nomeArquivo):
  try:      #Tentar fazer alguma coisa
    a = open(nomeArquivo, 'rt')
    a.close()
  except FileNotFoundError:  # Se der errado ira aparecer isso
    return False
  else:
    return True

# Função de listar os jogos e video games
def listarArquivo(nomeArquivo):
  try:
    a = open(nomeArquivo, 'rt')
  except:
    print('Erro ao abrir arquivo: ')
  else:
    print(a.read())  # Vai fazer o print de todos os arquivos na tela
  finally:   # Aqui fecha abrindo ou não o arquivo
    a.close()

# Função de cadastrar o jogos
def cadastrarJogo(nomeArquivo, nomeJogo, nomeVideogame):
  try:
    a = open(nomeArquivo, 'at')     # Salvar e preservar o conteudo
  except:
    print('Erro ao abrir o arquivo') # Se der erro
  else:
    a.write('{} | {}\n'.format(nomeJogo, nomeVideogame))
  finally:   # Aqui fecha abrindo ou não o arquivo
    a.close()

#Principal
arquivo = 'games.txt'  # O nome da variavel não interfere na função
if existeArquivo(arquivo):
  print('Arquivo encontrado no computador')
else:
  print('Arquivo enexistente')
  criaArquivo(arquivo)

while True:
  print('MENU')
  print('1 - Cadastrar novo item')
  print('2 - Listar cadastro')
  print('3 - Sair')

  op = valida_int('Escolha a opção desejada: ',1, 3)
  if op == 1:
    print('Opção de cadastrar no item selecionada...\n')
    nomeJogo = input('Nome do jogo: ')
    nomeVideogame = input('Nome do Videogame: ')
    cadastrarJogo(arquivo, nomeJogo, nomeVideogame)
  elif op == 2:
    print('Opção de listar selecionada...\n')
    listarArquivo(arquivo)
  elif op == 3:
    print('Encerrando o programa...')
    break




