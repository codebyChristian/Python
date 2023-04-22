def valida_int(pergunta, min, max):
  x = int(input(pergunta))
  while ((x < min) or (x > max)):
    x = int(input(pergunta))
  return x

def fatorial(num):
  fat = 1
  if num == 0:
    return fat
    # esta so sera executada caso num > 0
  for i in range(1, num+1, 1):
    fat *= i
  return fat

# principal
x = valida_int('Digite um numero para o fatorial:',0 , 99999)
print('{}! = {}: '.format(x, fatorial(x)))



#ttu
def realce(s1):   # Aqui é o corpo do parametro
  print('|','_'* 10,'|')
  print('|','_'* 10,'|')
  print(s1)
  print('|','_'* 10,'|')
  print('|','_'* 10,'|')

#Programa principal
realce('     Chris')  # Resolve em 1 linha de código


# h55
#Crie uma borda ao redor de uma palavra para destacá-la. A rotina deve receber
# como parâmetro a palavra a ser destacada.
# O tamanho da caixa deve ser adptável com o tamanho da caixa.

def borda(s1):
  tam = len(s1)
  # So imprime texto
  if tam:
    print('+','-' * tam,'+')
    print('|',s1,'|')
    print('+','-' * tam,'+')

#Programa pricipal
borda('Christian')
borda('Aprendendo funções e parâmetros')

#Faça uma função para validar uma string. Recebe como parâmetro a strig, o número mínimo e máximo de caracteres.
# Retorne verdadeiro se o tamanho da string estiver entre valores minimo e maximo, e falso,
# caso contrario(elaborando com base em Menezes, s.d)
def valida_string(pergunta,min, max):
  s1 = input(pergunta)
  tam = len(s1)
  while ((tam < min) or (tam > max)):
    s1 = input(pergunta)
    tam = len(s1)
  return s1
# principal
x = valida_string('Digite uma string: ',10, 30)
print('Você digitou: {}. \n Dado válido. Encerrando..'.format(x))
