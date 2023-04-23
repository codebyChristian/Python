
# Calcule o IMC: peso / (altura * altura)
# Abaixo do peso: 18.5
# Peso ideal: entre 18.5 e 25
# Sobrepeso: 25 até 30
# Obesidade: 30 até 40
# Obesidade mórbida: acima 40

print('DESCUBRAR SEU IMC')
print('PRECISAREMOS DO SEU PESO E ALTURA')
peso = float(input('Digite seu peso: (Kg)'))
altura = float(input('Digite sua altura:'))
Imc = peso / (altura * altura)  # Altura ao quadrado
print('Você tem IMC de \033[35m{:.2f}\033[m'.format(Imc))
if Imc < 18.5:
    print('ALERTA: \033[31mVocê está ABAIXO DO PESO\033[m')
elif 18.5 <= Imc <= 25:
    print('Esse é o \033[32mPESO IDEAL\033[m')
elif 25 <= Imc <= 30:
    print('Você está com \033[33mSOBREPESO\033[m')
elif 30 <= Imc <= 40:
    print('Você está com \033[34mOBSIDADE\033[m')
else:
    print('CUIDADO: Você está com \033[35mOBESIDADE MÓRBIDA\033[m')
