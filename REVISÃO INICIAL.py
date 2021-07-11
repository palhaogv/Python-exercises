#Faça 4 jogos aleatorios da mega sena

from random import (sample, shuffle)
n1 = input('Nome do primeiro jogador: ')
n2 = input('Nome do segundo jogador: ')
n3 = input('Nome do terceiro jogador: ')
n4 = input('Nome do quarto jogador: ')
l = [n1, n2, n3, n4]
shuffle(l)
print(f'A sequência da apresentação será: {l} ')