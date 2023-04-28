# Escreva uma função que calcule o fatorial
# de um número recebido como parâmetro e
# retorne o seu resultado
# Faça uma validação dos dados por meio de
# uma outra função, permitindo que somente
# valores positivos sejam aceitos

# Crie o help da sua função (exercício da
# apostila – aula 5)

def valida_int(pergunta, min, max): # Valida uma função
  x = int(input(pergunta))
  while ((x < min) or (x > max)):
    x = int(input(pergunta))
  return x

def fatorial(num):
  """
  Calcula a fatorial
  :param num: Número inteiro e positivo
  :return: Retorna 1º o número zero, e o 2º retorna um numero acima
  """
  fat = 1   # O menor fatorial é 1
  if num == 0:
    return fat  # Se digitar 0 vai resultar 1
    # esta so sera executada caso num > 0
  for i in range(1, num+1, 1):
    fat *= i  # fat = fat * i
  return fat

# principal
x = valida_int('Digite um numero para o fatorial:',0 , 9999)
print('{}! = {}: '.format(x, fatorial(x)))


