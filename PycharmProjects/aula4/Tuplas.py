linguagem = ('Rust', 'TypeScript', 'Python', 'Kotlin', 'Go',
             'Julia', 'Dart', 'C#', 'Swift', 'JavaScript')
print('Linguagens top 10 mais amadas de 2020')
for i in range(0, len(linguagem), 1):
    print(i+1, '-', linguagem[i])

print('\nTop 3:',linguagem[:3])
print('\nUltimos 5::',linguagem[-5:])
i = 0
while (linguagem[i] != 'Python'):
    i += 1
    print('Python esta na posição {}'.format(i+1))


