

#Desenvolva um programa que leia o comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input('Qual o comprimento da reta 1: '))
reta2 = float(input('Qual o comprimento da reta 2: '))             # CERTA
reta3 = float(input('Qual o comprimento da reta 3: '))
if reta1 > 0 and reta2 > 0 and reta3 > 0:  # Se alguma reta for igual a 0 não é possível forma um triangulo.
    if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
        print('Existe esse triângulo.')
    else:
        print('Não existe este triângulo com essas medidas:')
else:
    print('Não existe triângulo com reta 0.')

# -=-=-=-=-=-=-=-VERSÃO DIFERENCIADA-=-=-=-=-=-=-=

print('ANALISADOR DE TRIÂNGULOS')
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))    # Se uma reta for menor que a soma das outros duas retas não forma um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima formam um Triângulo:')
else:
    print('Esses segmentos não formam um Triângulo:')

