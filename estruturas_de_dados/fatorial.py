# Fatorial iterativo

def fatorial_iterativo(n):
    fat = 1
    if n < 0:    # Se for menor de 0 é vazio
        return None
    elif n == 0 or n == 1:
        return fat
    else:
        for i in range(1, n+1):
            fat *= i
        return fat
    

print(fatorial_iterativo(5))    

