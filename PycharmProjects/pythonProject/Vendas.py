fixo = 500
vendas = int(float(input('Quantos em reais voçê vendeu?')))
salario = 500 + (vendas * 6) / 100
print('Seu salario fixo é {} Reais.Como voçê vendeu {} Reais, seu salário é {} Comprimidos'.format(fixo, vendas, salario))