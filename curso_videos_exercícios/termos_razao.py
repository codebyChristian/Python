# Programa leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite qualquer número. > '))
pa = int(input('Qual será a razão. > '))
decimo = termo + (10 - 1) * pa   # O número 10, é quantos números vai aparecer
for c in range(termo, decimo + 1, pa):
    print(c, end=' > ')
print('Acabou')
# -------------volta
