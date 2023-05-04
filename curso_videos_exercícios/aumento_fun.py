# Crie um programa que vai receber o sálario de um funcionário e a % do aumento


print('Olá funcionário:')
salario = float(input('Qual é o seu sálario? R$'))
aumento = float(int(input('Qual é a porcentagem de aumento?')))
novo = (salario * aumento) / 100 + salario
print('O seu salário era {:.2f}R$: com o aumento de {}% ficou {:.2f}R$'.format(salario,aumento,novo))
