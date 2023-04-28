# ----------CONDIÇÕES ANINHADAS------------

# -------------------------------------------------------------------------
nome = str(input('Qual é seu nome? '))
if nome == 'Chris':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Jose' or nome == 'Jobescleiton':
    print('Esse nome é bastante popular!')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Este nome é bem louco!')
print('Tenha um Bom Dia, {}'.format(nome))
# --------------------------------------------------------------------