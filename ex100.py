#faça um programa que tenha um lista chamada numeros e duas funções:
# sorteio(): sortear 5 números e colocar dentro da lista.
# somapar(): vai mostar a soma entre todos os valores pares.

from random import randint


numeros = []


def sorteio(a, b):
    spar = 0
    print('Os números sorteados são: ', end=' ')
    for c in range(0, 5):
        s = randint(a, b)
        numeros.append(s)
        print(f'{s},', end=' ')
        if s % 2 == 0:
            spar += s
    print(f'\n A soma dos números pares é: {spar}')

sorteio(0, 999)

