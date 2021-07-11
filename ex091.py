#faça um jogo em que jogadores joguem um dado. Coloque o dic em ordem e mostre o ranking dos resultados

from time import sleep
from random import randint
jogos = {}
maior = 0

for c in range(0, 4):
    j = randint(1, 6)
    print(f'O {c+1}º jogador tirou {j}')
    jogos = {c: j}.copy()
    if j > maior:
        maior = j
print(jogos)
