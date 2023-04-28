# COMEÇO DA 1ª FUNÇAO

def dimensoesObjto():     # Essa função pede o comprimento, a largura e a altura. E retorna o valor em (dimensões) volume:
    while True:           # Crie um laço de repetição para caso ocorra algum erro ela volta para o ínicio:
        try:              # Tratativa de erro para caracteres não numericos :
            comp = float(int(input('Por favor digite o comprimento do objeto (em cm)> ')))
            largura = float(int(input('Por favor digite a largura do objeto (em cm)> ')))       # Essa três variáveis coletam as informações da 1ª linha
            altura = float(int(input('Por favor digite a altura do objeto (em cm):>')))
            if comp * largura * altura < 0:                                              # Crie uma condição que não aceita números negativos
                print('O volume é negativo. Tente novamente')
                continue                                                                 # Números negativos não são validos então repete as perguntas
            elif 0 < comp * largura * altura <= 1000:                                    # Crie uma condição aceita números entre 0 e 1000
                print('O volume é {:.1f}cm³:'.format(altura * comp * largura))           # Informa o volume
                return 10.00                                                             # Retorna o valor do volume
            elif 1000 < comp * largura * altura <= 10000:                                # Crie uma condição aceita números entre 1001 e 10000
                print('O volume é {:.1f}cm³:'.format(altura * comp * largura))
                return 20                                                                # Retorna o valor do volume
            elif 10000 < comp * largura * altura <= 30000:                               # Crie uma condição aceita números entre 10001 e 30000
                print('O volume é {:.1f}cm³:'.format(altura * comp * largura))
                return 30                                                                # Retorna o valor do volume
            elif 30000 < comp * largura * altura <= 100000:                              # Crie uma condição aceita números entre 30001 e 100000
                print('O volume é {:.1f}cm³:'.format(altura * comp * largura))
                return 50                                                                # Retorna o valor do volume
            else:                                                                        # Volumes acima de 100000 não são aceitos
                print('O volume é {:.1f}cm³: Não aceitamos objetos grandes.Tente novamante'.format(altura * comp * largura))
                continue
        except ValueError:
            print('Insira valores númericos: Tente novamente')
# FIM DA 1ª FUNÇAO


# COMEÇO DA 2 FUNÇÃO
def pesoObjto():   # Essa função pede o peso do objeto e retorna o multiplicador
    while True:    # Esta em um laço de repetição caso haja erro
        try:       # Tratativa de erro para caracteres não numericos:
            pesObjeto = float(input('Digite o peso do objeto em (Kg): '))     # Coleta o valor do peso
            if pesObjeto < 0:                                                 # Não aceita pesos negativos
                print('Não aceitamos pesos negativos. Tente novamente ')
            elif pesObjeto <= 0.1:                                            # Pesos de 0 a 0.1(Kg)
                return 1                                                      # Retorna o multiplicador
            elif 0.1 < pesObjeto <= 1:                                    # Pesos de 0.1 a 1(Kg)
                return 1.5
            elif 1 < pesObjeto <= 10:                                      # Pesos de 1 a 10(Kg)
                return 2
            elif 10 < pesObjeto <= 30:                                        # Pesos de 10 a 30(Kg)
                return 3
            else:                                                            # Pesos acima de 30(Kg) não é aceito
                print('Peso acima de 30Kg não é aceito. Tente outro peso: ')
                continue
        except ValueError:
            print('Digite valores numericos: Tente novamente')
            continue

# FIM DA 2ª FUNÇÃO

# COMEÇO DA 3ª FUNÇÃO
def rotaObejto():              # Essa função pede para selecionar a rota que está no menu e, retorna o multiplicador
    while True:
        rotaEscolher = input('Escolha a rota para o envio do objeto:\n'    # Mostra o menu e recebe a sigla escolhida
                             'RS - De Rio de Janeiro até São Paulo \n'
                             'SR - De São Paulo até Rio de Janeiro\n'
                             'BS - De Brasília até São Paulo\n'
                             'SB - De São Paulo até Brasília\n'
                             'PR - De Pernambuco até Rio de Janeiro\n'
                             'RP - Rio de Janeiro até Pernambuco\n>')
        if rotaEscolher == 'RS' or rotaEscolher == 'SR':                  # Por ter o mesmo multiplicador as duas siglas ficam juntas como as outras abaixo:
            return 1                                                      # Retorna o multiplicador
        elif rotaEscolher == 'BS' or rotaEscolher == 'SB':
            return 1.2
        elif rotaEscolher == 'PR' or rotaEscolher == 'RP':
            return 1.5
        else:
            print('Digite caracteres corretos...Tente novamente ')       # Um Tratamento de erro
            continue


# FIM DA 3ª FUNÇÃO

# COMEÇO DA 4ª FUNÇÃO (BÔNUS 4090111)
def ru4090111(borda):           # Nela cria uma borda adaptável com qualquer frase
    tam = len(borda)            # O (len) retorna o número de elementos dentro da borda
    print('|', '!' * tam,'|')
    print('!', borda, '!')     # E no programa principal a (borda) será adaptável
    print('|', '!' * tam, '|')

# FIM 4 FUNÇÃO (BÔNUS)

# PROGRAMA---PRICIPAL---


ru4090111('Bem-vindo ao PetShop do Christian Ernany Cardoso Dos Santos')          # Chamei a função com meu RU e com borda


dimensoes = dimensoesObjto()
print('O valor atual é {:.2f}R$'.format(dimensoes))             # A função retornou a valor em reais do volume


peso = pesoObjto()
print('O valor do multiplicador do Peso é {}'.format(peso))     # Retornou o multiplicar do peso

rota = rotaObejto()
print('O valor do multiplicador da Rota é {}'.format(rota))     # Retornou o multiplicar da rota

total = dimensoes * peso * rota         # Variável que recebe o valor total
print('----------------------------\n'
      'O valor a ser pago é {:.2f}R$\n'        # Um enfeite
      '----------------------------\n'
      '(Volume: {} * Peso: {} * Rota: {}'.format(total, dimensoes, peso, rota))
ru4090111('Obrigado por envia seu objeto conosco')
ru4090111('VOLTE SEMPRE')                                            # Chamei de novo a da borda adptável
