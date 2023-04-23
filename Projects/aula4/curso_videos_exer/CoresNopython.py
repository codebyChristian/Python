#text                    background            Style
#30      black       preto        40             0 none
#31      red         vermelho     41             1 Bold
#32      green       verde        42             4 Underline
#33      yellow      amarelo      43             7 Negative
#34      blue        azul         44
#35      Magenta     Magenta      45
#36      cyan        Ciano        46
#37      grey        Cinza        47
#97      white       Branco      107
# EXEMPLO \033[0;33;44m
# Começa uma cor \033[m ANSI

#print('\033[1;31;44mOlá, Mundo\033[m')
#print('\033[4;30;45mOlá, Mundo\033[m')
#print('\033[7;97;40mOlá, Mundo\033[m')  # o 7 inverte

#a = 4
#b = 2
#print('Os valores são \033[4;36m{}\033[m e \033[4;33m{}\033[m !!!'.format(a, b))

nome = 'Christian'
cores = {'limpar': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;107m'}
print("How are you, {}{}!!".format(cores['azul'], nome, cores['limpar']))

