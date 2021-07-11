#faça um programa que ajude um jogar a criar palpites para mega-sena.
#O programa deve perguntar quantos jogos fará. 6 numeros para cada jogo de 1 a 60 .
#Castrando tudo numa lista composta
from random import randint
jogind = []
jogos =[]
print('Olá, Jogador!')
n = int(input('Quantos jogos você quer fazer? '))

for j in range(0, n):
    for c in range(0, 7):
        r = randint(1, 61)
        while True:
            if r not in jogind:
                jogind.append(r)
                break
            else:
                r = randint(1, 61)
    jogind.sort()
    print(f'O {j+1}º jogo: {jogind}')
    jogos.append(jogind[:])
    jogind.clear()


