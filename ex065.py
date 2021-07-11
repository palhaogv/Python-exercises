#Faça um programa que pergunte ao usuario varios números inteiros.
# O programa deve trazer a média de todos os números, o maior e o menor valor
# e perguntar ao usuários se ele quer continuar.

qt = int(input('Quantos números você quer analisar? '))
count = 1
s = 0
maior = 0
menor = 0
while count <= qt:
    n = int(input(f'Digite o valor número {count}: '))
    count += 1
    s += n
    if count == 2:
        maior = n
        menor = n
    if maior < n:
        maior = n
    elif menor > n:
        menor = n

print(f'Os {qt} números somados são iguais a {s}. O maior número digitado é {maior} e o menor, {menor}. '
      f'\nA média entre eles é de {s/qt}')