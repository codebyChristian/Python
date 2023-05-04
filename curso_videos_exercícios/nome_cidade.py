#024: Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade:')).strip()  
fatia = cidade.strip()
print(fatia[0].upper() in 'SANTO')


#  DICAS DO PROFESSOR
#city = input('Nome da cidade:').strip()  # elimina espaços indejejados
#print(city[:5].upper() == 'SANTO')   
