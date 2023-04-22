listadeEstudandes = []

#---------COMEÇO DA FUNÇAO CADASTRARESTUDANTE------
def cadastrarEstudante(ru):
  print('Bem vindo ao CADASTRAR estudantes:')
  print('O RU a ser cadastrado é: {}'.format(ru))
  nome = input(('Digite o nome do estudante: '))
  turma = input('Digite a turma do estudante: ')
  dicionarioEstudante = {'ru': ru,
                         'nome': nome,
                         'turma': turma}
  listadeEstudandes.append(dicionarioEstudante.copy())

#---------FIM DA FUNÇAO CADASTRARESTUDANTE------

#---------COMEÇO DA FUNÇAO CONSULTARESTUDANTE------
def consultarEstudante():
  while True:
    try:
      print('Bem vindo ao CONSULTAR estudante:')
      opConsultar = int(input('Entre com a opção:\n'
                              '1- Consultar Todos os Estudantes\n'
                              '2- Consultar por RU\n'
                              '3- Consultar por Turma\n'
                              '4- Retornar'
                              '>'))
      if opConsultar == 1:
        print('Bem vindo a consultar TODOS')
        for estudante in listadeEstudandes:  # selecionar cada dicionario da lista
          for key, value in estudante.items(): # selecionar cada conjunto chave do dicionario
            print('{} : {} '.format(key,value))
      elif opConsultar == 2:
        print('Bem vindo a Consultar por RU')
        entrada = int(input('Digite o RU desejado: '))
        for estudante in listadeEstudandes:
          if(estudante['ru'] == entrada):
            for key, value in estudante.items():
              print('{} : {} '.format(key,value))
      elif opConsultar == 3:
        print('Bem vindo a Consultar por Turma')
        entrada = input('Digite a TURMA desejado: ')
        for estudante in listadeEstudandes:
          if(estudante['turma'] == entrada):
            for key, value in estudante.items():
              print('{} : {} '.format(key,value))
      elif opConsultar == 4:
        return
      else:
        print('Número não encontado. Tente novamente:')
    except ValueError:
      print('Digite números do menu:')

#----------FIM DA FUNÇAO CADASTRARESTUDANTE------

#---------COMEÇO DA FUNÇAO REMOVERESTUDANTE------
def removerEstudante():
  print('Bem vindo ao REMOVER estudante:')
  entrada = int(input('Digite o RU desejado: '))
  for estudante in listadeEstudandes:
    if(estudante['ru'] == entrada):
      listadeEstudandes.remove(estudante)

#---------FIM DA FUNÇAO REMOVERESTUDANTE------

#-----PRINCIPAL-------
print('Bem-vindo ao programa Controle de alunos de Christian Santos')
registroAcademico = 0
while True:
  try:
    opcao = int(input('Digite a opção desejada:\n'
                      '1-Cadastrar Estudante\n'
                      '2-Consultra Estudante\n'
                      '3-Remover Estudante\n'
                      '4-Sair'
                      '>'))
    if opcao == 1:
      registroAcademico = registroAcademico + 1
      cadastrarEstudante(registroAcademico)
    elif opcao == 2:
      consultarEstudante()
    elif opcao == 3:
      removerEstudante()
    elif opcao == 4:
      print('Programa finalizado:')
      break
    else:
      print('Número não encontado. Tente novamente:')
  except ValueError:
    print('Digite números do menu:')
    continue