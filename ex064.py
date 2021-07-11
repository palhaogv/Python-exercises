#digite um programa que leia varios números inteiros, o programa só deve parar quando o usuário digitar 999.
# No final, mostre quantos números foram digitados e qual a soma entre eles.(desconsideradno o flag).

n = int(input('Digite um número inteiro: '))
cont = 1
soma = n

while n != 999:
    n = int(input('Digite outro número inteiro: '))
    cont += 1
    soma += n
print(f'A quantidade de números digitados foi de {cont} e a soma deles foi {soma}!')

