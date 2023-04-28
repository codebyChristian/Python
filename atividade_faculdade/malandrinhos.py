boneco = int(float(input('Quantos Bonecos Malandrinhos vendidos:')))
peque = int(float(input('Quantos Spinner Pequeno vendidos:')))
cubo = int(float(input('Quantos Cubos Magicos vendidos:')))
valor = boneco * 18.50 + peque * 12.00 + cubo * 5.90
print('Voçê faturou {0:2}'.format(valor))