listadePecas = []  # Uma lista para armazenar cadastros

#---FUNÇÃO--DE--CADRASTRARPECA-- (-Essa função pede informações para cadastra a peça-)
def cadastrarPeca(codigo):
    print('Selecionado Cadastra Peça:')
    print('O código da peça a ser cadastrado é {}:'.format(codigo),)  # É mostrada o código da peça
    nome = input('Digite o nome da peça:')
    fabricante = input('Digite o fabricante da peça:')
    valor = int(input('Qual o valor da peça:'))
    dicionarioPecas = {'codigo': codigo,       # Os dados da peça são armazenados neste dicionário
                       'nome': nome,
                       'fabricante': fabricante,
                       'valor': valor,}
    listadePecas.append(dicionarioPecas.copy()) # Aqui o dicionário é adicionado dentro da lista global

#---FIM--DA--FUNÇÃO--DE--CADRASTRARPECA--

#---FUNÇÃO--DE--CONSULTARPECAS--(-Essa função tem o menu de consulta de peças-)
def consultarPeca():
    while True:
        try:                                       # Menu secúndario
            print('Selecionado Consultar Peças:')
            consultPeca = int(input('|1 - Consultar Todas as Peças      |\n'
                                    '|2 - Consultar Peças por Código    |\n'
                                    '|3 - Consultar Peças por Fabricante|\n'
                                    '|4 - Retornar                      |\n'
                                    ' >>'))
            if consultPeca == 1:
                print('-' * 25)
                print('Aqui esta todas as peças: ')
                for bike in listadePecas: # Procura cada dicionário da lista de peça,
                    for key, value in bike.items(): # Então peço a chave e o valor de todos os itens do dicionário
                        print('-' * 25)
                        print('{} : {} '.format(key,value))
            elif consultPeca == 2:
                print('Consulta por código:')
                ru4090111 = int(input('Digite o codigo da peça: '))
                for bike in listadePecas:
                    if(bike['codigo'] == ru4090111):  # Se o código digitado estiver na lista de dicionários,
                        for key, value in bike.items():  # Ele será mostrado
                            print('-' * 25)
                            print('{} : {} '.format(key,value))
                            print('-' * 25)
                    else:           # Isso será mostrado caso o código não esteja na lista
                        print('Código não encontrado:')
            elif consultPeca == 3:
                print('Consulta peças por fabricante:')
                ru4090111 = input('Digite o nome do fabricante:')
                for bike in listadePecas:
                    if(bike['fabricante'] == ru4090111):      # Se a fabricante digitada estiver na lista de dicionários,
                        for key, value in bike.items():       # Será mostrada
                            print('-' * 25)
                            print('{} : {} '.format(key,value))
                            print('-' * 25)
                    else:
                        print('Fabricante não encontrado:')
            elif consultPeca == 4:                             # Vai retorna para o menu inicial
                return
            else:                                               # Tratamento de erro
                print('Número invalido...Tente novamente:')
                continue
        except ValueError:                                      # Tratamento de erro
            print('Caracteres invalidos...Tente novamente:')
            continue


#---FIM--DA--FUNÇÃO--DE--CONSULTARPECAS--

#---FUNÇÃO--DE--REMOVERPECAS--
def removerPeca():
    print('Selecionado Remover Peça:')
    a4090111 = int(input('Insira o código a ser removido:'))
    for bike in listadePecas:   # Se o código digitado estiver na lista de dicionários,
        if(bike['codigo'] == a4090111):
            listadePecas.remove(bike) # Será removido da lista
            print('Peça removida com sucesso:')

#---FIM--DA--FUNÇÃO--DE--REMOVERPECAS--


#----PROGRAMA---PRINCIPAL----------
print('-' * 82)
print('Bem-vindo ao controle de peças da bicicletaria Christian Ernany Cardoso dos Santos')
print('-' * 82)
pecasRegistro = 0        # Começa em zero e irá aumentando a cada cadastro
while True:
    try:
        opcao = int(input('Escolha uma das opções disponiveis:\n'  # Menu principal
                '|1 - Cadastrar Peças|\n'
                '|2 - Consultar Peças|\n'
                '|3 - Remover Peças  |\n'
                '|4 - Sair           |\n'
                ' >>'))
        if opcao == 1:
            pecasRegistro = pecasRegistro + 1            # Começa em zero e irá aumentando a cada cadastro
            cadastrarPeca(pecasRegistro)                 # Chama a função de cadastrar peça
        elif opcao == 2:
            consultarPeca()                              # Chama a função de consultar peça
        elif opcao == 3:
            removerPeca()                                # Chama a função de remover peça
        elif opcao == 4:
            print('Programa finalizado...')              # Tratamento de erro
            break
        else:
            print('Número invalido...Tente novamente:')
    except ValueError:                                   # Tratamento de erro
        print('Caracteres invalidos...Tente novamente:')
        continue

