nota1 = float(input('Qual sua primeira nota: '))
nota2 = float(input('Qual sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua média é {:.1f}'.format(media))
print('Parabens' if media >=6 else 'Reprovado!')   # Forma simples mas confusa
if media >= 7:
    print('Parabens, você foi aprovado!')
else:
    print('Se lascou foi Reprovado:')