# Leia o sexo de uma pessoa, mas só aceite os valores M ou F.
# Se digitar outra letra faça repetir o programa

print('M para \033[36mMASCULINO\033[m e F para \033[35mFEMININO\033[m\n'
      'Qualquer outro não será aceito!')
n = 1
while n != 'F' and n != 'M':
    n = str(input('Sexo: [M/F] >')).upper()[0].strip()
    if n != 'F' and n != 'M':
        print('Dados invalidos. Tente novamente...')
print('Sexo {} registrado'.format(n))


# Professor
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in '[M/F]':
    sexo = str(input('Dados inválidos. Por favor, tente de novo '))
print('Sexo {} registrado com sucesso'.format(sexo))
