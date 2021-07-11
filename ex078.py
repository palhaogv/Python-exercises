#faça um programa que leia 5 valores numericos e guarde-os em uma lista
#no final, mostre o maior e o menor valor digitado e suas devidas posições

lista = list()
maior = 0
menor = 0
for l in range(0,5):
    n = int(input('Digite um número inteiro: '))
    if maior == 0:
        maior = n
    if menor == 0:
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    lista.append(n)
print(f'A lista digitada é: {lista}\n'
      f'O maior valor é: {maior}\n'
      f'O menor valor é: {menor}')