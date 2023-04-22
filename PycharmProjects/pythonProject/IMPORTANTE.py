#------ATIVIDADE PRÁTICA 1------- RU:4090111------------
print('Bem Vindo a loja de Christian Ernany Cardoso Dos Santos:          (RU:4090111)\n'    # Utilizei a quebra no print 
      'Veja nossa tabela de descontos:\n'                       # Usei o print desta maneira porque vi na apostila de orientações gerais
      'Até 9 unidades não terá desconto:\n'                     # Coloquei a tabela de descontos para o usuário 
      'Entre 10 e 99 terá 5% por cento de desconto:\n'
      'Entre 100 e 999 terá 10% por cento de desconto:\n'
      'Acima de 1000 terá 15% por cento de desconto:')
valorProdu = float(input('Agora que voçê escolheu o produto digite o valor dele:R$'))  # Variável para receber o preço
quantProdu = int(input('Quantas unidades foram escolhidas:'))              # Variável para receber s quantidade
subtotal = valorProdu * quantProdu               # Esta variável armazena o valor sem desconto
if quantProdu <= 9:                              # Utizada a estrutura if como pedido na questão
    valorFinal = subtotal                        # Até 9 unidades não há desconto
    print('O valor final é {}$:\n'
          'Obrigado por comprar conosco:\n'
          'Volte sempre:'.format(valorFinal))
elif 10 <= quantProdu <= 99:                                 # Utilizada a estrutura elif como pedido na questão
    valorFinal = subtotal - subtotal * 0.05                  # Houve desconto de 5%
    print('O valor sem desconto é {:.2f}$:\n'                # Utilizada a formatação com 2 casas decimais
          'O valor com desconto é {:.2f}$: (Desconto de 5%)\n'
          'Obrigado por comprar conosco:\n'
          'Volte sempre'.format(subtotal, valorFinal))
elif 100 <= quantProdu <= 999:
    valorFinal = subtotal - subtotal * 0.10                  # Houve desconto de 10%
    print('O valor sem desconto é {:.2f}$:\n'
          'O valor com desconto é {:.2f}$: (Desconto de 10%)\n'
          'Obrigado por comprar conosco:\n'
          'Volte sempre'.format(subtotal, valorFinal))
else:
    valorFinal = subtotal - subtotal * 0.15                 #   Utilizada a estrutura elif como pedido na questão
    print('O valor sem desconto é {:.2f}$:\n'
          'O valor com desconto é {:.2f}$: (Desconto de 15%)\n'
          'Obrigado por comprar conosco:\n'
          'Volte sempre'.format(subtotal, valorFinal))