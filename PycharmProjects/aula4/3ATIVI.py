# ----COMEÇO DA FUNÇÃO DIMENSOESOBJETO----
def dimensoesObejto():
    try:
        altur = int(input('Por favor digite a altura do objeto em (cm)>>'))
        largu = int(input('Por favor digite o comprimento do objeto em (cm)>>'))
        compri = int(input('Por favor digite a largura do objeto em (cm):>>'))
        return altur * largu * compri
    except ValueError:
        print('Digite um valor númerico:')
# ----FIM DA FUNÇÃO DIMENSOESOBJTO-------

# ----COMEÇO DA FUNÇÃO PESOOBJETO---------
def pesoObjto():
    while True:
        try:
            pesObjeto = float(input('Digite o peso do objeto em (Kg): '))
            if  pesObjeto <= 0.1:
                return 1
            elif 0.10 < pesObjeto <= 1:
                return 1.5
            elif 1.09 < pesObjeto <= 10:
                return 2
            elif 10 < pesObjeto <= 30:
                return 3
            else:
                print('Peso acima de 30Kg não é aceito. Tente outro peso: ')
                continue
        except ValueError:
            print('Digite valores numericos: Tente novamente')
            continue
# ----FIM DA FUNÇÃO PESOOBJETO------------

# ----COMEÇO DA FUNÇÃO ROTAOBJETO---------
def rotaObejto():
    while True:
        rotaEscolher = input('Escolha a rota para o envio do objeto:\n'
                             'RS - De Rio de Janeiro até São Paulo \n'
                             'SR - De São Paulo até Rio de Janeiro\n'
                             'BS - De Brasília até São Paulo\n'
                             'SB - De São Paulo até Brasília\n'
                             'PR - De Pernambuco até Rio de Janeiro\n'
                             'RP - Rio de Janeiro até Pernambuco\n>')
        if rotaEscolher == 'RS' or 'SR':
            return 1
        elif rotaEscolher == 'BS' or 'SB':
            return 1.2
        elif rotaEscolher == 'PR' or 'RP':
            return 1.5
        else:
            print('Digite caracteres corretos...Tente novamente ')
            continue
# ----FIM DA FUNÇÃO ROTAOBJETO------------

# ----COMEÇO DO PROGRAMA PRINCIPAL--------
print('Bem-vindo ao PetShop do Christian Ernany C. Dos Santos')
volum3 = dimensoesObejto
print(volum3)

#while True:
#    if 0 < volume <= 1000:
#        return 10
#    elif 1000 < volume <= 10000:
 #       return 20
  #  elif 10000 < volume <= 30000:
#        return 30
#    elif 30000 < volume <= 100000:
 #       return 50
  #  else:
   #     print('Não aceitamos objetos com estas dimensõe:')
    #    continue

#peso = pesoObjto()
#melhoRota = rotaObejto()
#total = volum3 * peso * melhoRota
#print('O valor final é: R$ {:.2f}'.format(total))
# ----FIM DO PROGRAMA PRINCIPAL--------
