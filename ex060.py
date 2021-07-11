#faça um programa que leia um número qualquer e faça seu fatorial
#ex: 5! = 5*4*3*2*1
n = int(input('Digite um número inteiro: '))
m = n
f = 1
print(f'O {n}! = ', end='')
while m > 0:
    print(f'{m}', end='')
    print(' x 'if m > 1 else ' = ', end='')
    f = f*m
    m -= 1
print(f'{f}')




