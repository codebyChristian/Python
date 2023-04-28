# Escreva um programa que leia a velocidade de um carro
# Se ele ultrapassar 80Km/, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00
# por cada Km acima do limite.

veloz = float(input('A velocidade do carro é > '))
if veloz > 80:
    print('Você está sendo multado...'
          'Você excedeu o limite de 80Km/h'
          'Você irá pagar uma multa!')
    nume = veloz - 80    # multa = (veloz - 80) * 7 Támbem serve
    print('O valor da multa é {:.2f} Reais:'.format(nume * 7))
else:                # Não precisa usar else é facultativo
   print('Um bom dia e dirija com segurança::')