#faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
from random import randint
n = int(input('Digite um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000
print(f'{n}')
print(f'A unidade de {n} é: {u}')
print(f'A dezena de {n} é: {d}')
print(f'A centena de {n} é: {c}')
print(f'O milhar de {n} é: {m}')