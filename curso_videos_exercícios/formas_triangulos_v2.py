
# Refaça desafio 35 do triângulo, dizendo como será ele
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

print('Descubrindo os TRIÂNGULO:')
reta1 = float(input('Digite a Primeira reta do triângulo: '))
reta2 = float(input('Digite a Segunda reta do triângulo: '))
reta3 = float(input('Digite a Terceira reta do triângulo: '))
print('O triângulo com retas {:.0f}, {:.0f}, {:.0f}'.format(reta1, reta2, reta3))
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
   print('Ele pode forma um TRIÂNGULO:', end=' ')
   if reta1 == reta2 == reta3:
       print('Esse Triângulo é \033[32mEQUILÁTERO\033[m')
   elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
       print('Esse Triângulo é \033[33mISÓSCELES\033[m')
   elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
       print('Esse Triângulo é \033[34mESCALENO\033[m')
   else:
       print('ASSISTA SOUTH PARK:')
else:
   print('\033[35mNão é possivel forma um TRIÂNGULO\033[m:')
