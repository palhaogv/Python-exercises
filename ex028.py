#Escreva um programa em que o computador escolhe um valor aleatorio e peça para o usuário adivinhar
#o programa deverá informar se foi o usuário acertou ou errou

from random import randint
n = randint(1,5)
u = int(input('Digite um número inteiro de 0 a 5 e tente acertar o número selecionado pelo PC: '))
if n==u:
    print(f'PARABÉNS, o computador escolheu {n} e você GANHOU!')
else:
    print(f'Você errou, o computador escolheu {n} :(. Tente novamente.')
