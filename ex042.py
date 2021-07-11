#desenvolva um programa que informe se o comprimento de 3 retas formam um triângulo.
# caso forme um triangulo, informe se ele é equilátero, isóceles ou escaleno.

from math import sqrt

a = float(input('Digite a medida da reta "a" : '))
b = float(input('Digite a medida da reta "b" : '))
c = float(input('Digite a medida da reta "c" : '))
a1 = sqrt((c**2 + b**2))
b1 = sqrt((a**2 + c**2))
c1 = sqrt((b**2 + a**2))

if b + c > a > a1 or a + c > b > b1 or a + b > c > c1 and a == b != c or a == c != b or b == c != a:
    print(f'Essas retas formam um triângulo isóceles.')
elif b + c > a > a1 or a + c > b > b1 or a + b > c > c1 and a == b == c or a == c == b or b == c == a:
    print(f'Essas retas formam um triângulo equilátero.')
elif b + c > a > a1 or a + c > b > b1 or a + b > c > c1 and a != b != c:
    print(f'Essas retas formam um triângulo escaleno.')
else:
    print(f'Essas retas não formam um triângulo.')

