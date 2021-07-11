#Faça o programa 028 novamente com o computador escolhendo um valor de 0 a 10.
# Na hr que o usuario acertar o numero do PC, o jogo para e diz quantas vezes foram necessárias.

from random import randint
n = 0
pc = randint(1, 10)
count = 0
while n != pc:
    if n == 12:
        n = int(input('Digite um número inteiro de 1 a 10 e tente acertar o número selecionado pelo PC: '))
    else:
        n = int(input('Você errou, tente novamente: '))
    count += 1
if count == 1:
    print(f'Parabéns, você acertou de primeira!')
else:
    print(f'Parabéns, você acertou em {count} tentativas.')
