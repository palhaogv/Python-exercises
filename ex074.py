#crie uma tupla com 5 numeros aleatorios e mostre qual o menor e o maior. Mostre a listagem
from random import randint

seq = randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000), randint(0,1000),
maior = 0
menor = 0
cont = 0
print(seq)
while cont < 5:
    if cont == 0:
        maior = seq[cont]
        menor = seq[cont]
    if seq[cont] > maior:
        maior = seq[cont]
    elif seq[cont] < menor:
        menor = seq[cont]
    cont += 1
print(f'O maior número é {maior}, e o menor número da lista é {menor}.')


