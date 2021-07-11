#Crie um programa que o usuario digite um numero de 0 a 20 e o programa leia ele por extenso.
#Caso o usuário digite um valor fora de range, o programa deve mandar digitar de novo

seq = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'dose', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    n = int(input('Digite um número de 0 à 20: '))
    if 0 <= n <= 20:
        print(f'{seq[n]}')
        break
    else:
       print('Você não digitou um número entre 0 e 20.')
print('FIM.')