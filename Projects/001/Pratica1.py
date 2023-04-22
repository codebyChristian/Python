# 1
preco = input('Qual o preço do produto filhinho!!?')
desconto = input('Qual foi seu desconto? engenheiro!')
preco = float(preco)
desconto = float(desconto)
desconto = preco * (desconto / 100)
final = preco - desconto
print('O preço é {} Reais.Desconto de {}% Porcentos.'.format(preco, desconto))
print('O valor do desconto é {}. O valor final é {} Reais.'.format(desconto, final))
