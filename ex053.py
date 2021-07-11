# crie um programa que leia um frase e diga se ela é palindromo desconsiderando espaços.

g = str(input('Digite uma frase: ')).upper().strip()
s = g.split()
j = ''.join(s)
i = j[::-1]
if j == i:
    print(f'Essa frase é um PALÍNDROMO, olha só {j} é igual a {i} ao contrário.')
else:
    print(f'O inversor de {j} é {i}. Essa frase não é um PALÍNDROMO.')
