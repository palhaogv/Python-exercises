#faça um programa que leia um n inteiro e diga se ele é ou não primo
n = int(input('Digite um número inteiro: '))
s = 0

for c in range (1,n+1):
    if n % c ==0:
        print('\33[33m', end='')
        s += 1
    else:
        print('\33[31m', end='')
    print(f'{c} ', end='')
print(f'\n\33[mO número {n} foi dividido {s}x.')
if s > 2:
    print('Logo, esse número não é PRIMO!')
else:
    print('Logo, esse número é PRIMO')