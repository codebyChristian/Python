
# Escreva um programa que pergunte o salário de um funcionário e calcule
# o valor do seu aumento. Para salários superiores a R$1.250,00, calcule
# um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.

salario = float(input('Seu salário em REAIS: R$ '))
if salario >= 1.250:       # ERRADO
    novo = (salario * 0.10) + salario
    print('Com o aumento você deixou de receber {:.2f} e agora vai ganhar {:.2f} Reais'.format(salario, novo))
else:
    nov = (salario * 0.15) + salario
    print('Com o aumento você deixou de receber {:.2f} e agora vai ganhar {:.2f} Reais'.format(salario, nov))

# versão do diferente

salario = float(input('Qual é o seu salário em REAIS: R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Você ganhava {:.2f} agora vai receber {:.2f}:'.format(salario, novo))
