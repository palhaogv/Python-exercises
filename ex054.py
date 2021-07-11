# crie um programa que leia o ano de nascimento de 7 pessoas e informe quais são maiores de idade e quais não

for c in range (1, 8):
    i = int(input('Digite o ano que você nasceu: '))
    if 2020 - i > 18:
        print(f'\33[31mVocê é maior de idade.\33[m')
    else:
        print(f'\33[33mVocê não é maior de idade.\33[m')

