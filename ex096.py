#faça uma função chamada area, que calcule a area de um terreno retangular
def area(a, b):
    c = a*b/2
    print(f'A área é {c}m².')

c = float(input('Qual a altura? '))
d = float(input('Qual a base? '))
area(c, d)

