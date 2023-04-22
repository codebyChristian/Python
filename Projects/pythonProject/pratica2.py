frase = input('Escreva qualquer frase:')
tam = len(frase)
frase2 = frase[:int(tam/2)] # Essa ele divide a frase no meio
print(frase2)
# Pegar as 2 ultimas letras
print(frase2[-2:])

# resolver depois

a = int(float(input('Quantos reais por hora:')))
b = int(float(input('Quantas horas trabalhou:')))
c = int(float(input('Quantas horas de extra:')))
sala = c * (2 * a) + a * b
print(sala)
