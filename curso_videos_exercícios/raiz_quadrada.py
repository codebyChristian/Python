# Programa receber um número e irá mostra a raiz quadrada

import math
num = int(input('Digite um número:'))
raiz = math.sqrt(num)                                      # math.floor(raiz))) Arrendonda para baixo
print('A raiz de {} é igual {}'.format(num, math.ceil(raiz)))    

                                                             # math.ceil(raiz))) Arredonda a raiz para cima


# FORMA PARECIDA

from math import sqrt   # Adicionar , e outra função
num = int(input('Digite um número:'))
raiz = sqrt(num)                                              # math.floor(raiz))) Arrendonda para baixo
print('A raiz de {} é igual {}'.format(num, raiz))     # math.ceil(raiz))) Arredonda a raiz para cima

