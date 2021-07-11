#Escreva um programa que leia dois números e informe qual deles é maior ou se são iguais.

from random import randint

a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))

if a > b:
    print(f'O número {a} é maior do que {b}!')
elif a < b:
    print(f'O número {a} é menor do que {b}!')
elif a == b:
    print(f'O valor dos dois números são iguais')