a = int(input('Qual o lado da triangulo:'))
b = int(input('Qual o lado da triangulo:'))
c = int(input('Qual o lado da triangulo:'))
if (a > 0 and b > 0 and c > 0):
    if (a + b > c and a + c > b and b + c > a):
        if a != b and a != c and b != c:
            print('É escaleno:')
        else:
            if a == b and a == c and b == c:
                print('É equilatero')
            else:
               print('É isosceles')
    else:
        print('Deu erro ja era')
else:
    print('Triangulo invalido')

