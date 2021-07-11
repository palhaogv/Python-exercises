#Escreva um programa que de um número inteiro aleatório e peça para o usuário escolher
# se a conversão será:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

from random import randint

n = randint (0,9999)
resp = str(input(f'Para o número {n}, você deseja converter para binário, octal ou hexadecimal? ')).lower().strip()
if resp == 'binário':
    print(f'Binário: \033[1;40;37m{bin(n)}\033[m !')
elif resp == 'octal':
    print(f'Octal: \033[1;40;37m{oct(n)}\033[m !')
elif resp == 'hexadecimal':
    print(f'Hexadecimal: \033[1;40;37m{hex(n)}\033[m !')
