# crie um programa que leia o ano de nascimento de 7 pessoas e informe qts são maiores de idade e qts menores

from datetime import date

count = 0
for c in range (1, 8):
    n = int(input(f'Quando a {c}ª pessoa nasceu? '))
    i = date.today().year - n
    if i >= 18:
        count += 1
print(f'Existem {count} pessoas maiores de idade e {7 - count} menores de idade.')