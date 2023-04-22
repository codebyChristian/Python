somatoria = 0   # Essa variável fica fora do laço porque ela determina que a contagem inicie em 0
a = 0           # Caso isso não aconteça o programa não corresponde com que é pedido
print('Seja bem-vindo a lanchonete Christian Ernany Cardoso Dos Santos\n'
    '-------------OPÇÕES DE PRODUTOS-----------------\n'
    '|CÓDIGO| |       DESCRIÇÃO       | | VALOR(R$) |\n'
    '| 100  | |    Cachorro-Quente    | |   9,00    |\n'
    '| 101  | | Cachorro-Quente Duplo | |   11,00   |\n'     # Menu para o usuário escolher e selecionar
    '| 102  | |         X-Egg         | |   12,00   |\n'
    '| 103  | |       X-Salada        | |   13,00   |\n'
    '| 104  | |        X-Bacon        | |   14,00   |\n'
    '| 105  | |        X-Tudo         | |   17,00   |\n'
    '| 200  | | Refrigerante de Lata  | |   5,00    |\n'
    '| 201  | |      Chá Gelado       | |   4,00    |\n')
while a == 0:    # Inicia o laço de repetição
    codigo = input('Entre com o código do produto desejado: ') # Pede somente o código do produto
    if codigo == '100':
        somatoria = somatoria + 9.00   # Se esse código for selecionado irá adicionar 9 Reais na conta
    elif codigo == '101':
        somatoria = somatoria + 11.00  #  Se esse código for selecionado irá adicionar 11 Reais na conta
    elif codigo == '102':
        somatoria = somatoria + 12.00  #  Se esse código for selecionado irá adicionar 12 Reais na conta
    elif codigo == '103':
        somatoria = somatoria + 13.00  # Se esse código for selecionado irá adicionar 13 Reais na conta
    elif codigo == '104':
        somatoria = somatoria + 14.00  # Se esse código for selecionado irá adicionar 14 Reais na conta
    elif codigo == '105':
        somatoria = somatoria + 17.00  # Se esse código for selecionado irá adicionar 15 Reais na conta
    elif codigo == '200':
        somatoria = somatoria + 5.00  # Se esse código for selecionado irá adicionar 5 Reais na conta
    elif codigo == '201':
        somatoria = somatoria + 4.00  # Se esse código for selecionado irá adicionar 4 Reais na conta
    else:
        print('Código invalido...Por favor tente novamente:')  # Qualquer outro caractere não identificado irá aparece essa mensagem
        continue                                               # Depois do erro essa função retorna e pede novamente o código correto
    print('O valor a ser pago está em: {:.2f}R$'.format(somatoria))  # Esse print resulta na conta atual do cliente

    resposta = input('Deseja algo mais:\n'
                     '1 - NÃO\n'
                     '2 - SIM\n'
                     '')
    if resposta == '1':    # Caso for 's' o programa volta para o começo do laço 'while'
        continue
    elif resposta == '2':   # Caso for 'n' o programa vai para fase final
        print('O valor final da conta é: {:.2f}R$'.format(somatoria))   # Mostrar a conta final ao cliente
        break
    else:
        print('Código invalido:')  # Se for digitado qualquer outro caractere vem esta mensagem

