#crias uma lista com 7 numeros inteiros que separe impar e par e dps printar de forma crescente esse numeros
from random import randint
lista_num = []
lista_impar = []
lista_par = []

for a in range (0,7):
    n = randint(0,30)
    print(f'{n} ', end='')
    lista_num.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    elif n % 2 != 0:
        lista_impar.append(n)
print(f'\nA lista de números sorteados é: {lista_num}\n'
      f'Esses são os números pares {lista_par}\n'
      f'Esses são os números ímpares {lista_impar}.')

