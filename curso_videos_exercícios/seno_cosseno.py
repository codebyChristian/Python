# Qual seno e cosseno

import math  (from math import radians, sin, cos, tan

num = float(input('Digite o ângulo logo:'))
seno = math.sin(math.radians(num))
print('O ângulo de {} tem SENO de {:.2f} '.format(num, seno))
cosseno = math.cos(math.radians(num))
print('O ângulo de {} tem COSSENO de {:.2f} '.format(num, cosseno))
tangente = math.tan(math.radians(num))
print('A ângulo de {} tem TANGENTE de {:.2f} '.format(num, tangente))
