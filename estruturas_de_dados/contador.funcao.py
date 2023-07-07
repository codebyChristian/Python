
def chris_sequencial(elemento,sequencia):  # 
    count = 0                           # inicia com 0
    for item in sequencia:
        if item == elemento:            # se for igual
            count += 1                  # itera um na contagem
    return count                        # retorna o valor da ocorrências do nº desejado

# programa principal

nota_pratica = [23,4,67,54,90,21,54,5,29,54]
ocorrencias = chris_sequencial(54, nota_pratica)       # lista quantas vezes o 6 aparecer
print(ocorrencias)
