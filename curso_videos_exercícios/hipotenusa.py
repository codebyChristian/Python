# Leia o comprimento do cateto oposto e o cateto adjacente, e calcule a hipotenusa

from math import hypot
oposto = float(input('Digite o cateto oposto do triângulo:'))
adja = float(input('Digite o cateto adjacente do triângulo:'))
print('O cateto oposto é {}, e cateto adjacente é {}: Então a hipotenusa será {:.2f}'.format(oposto, adja, hypot(oposto, adja) ))

# Sem importação

co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir: {:.2f}'.format(hi))
