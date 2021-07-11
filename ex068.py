#faça um jogo que o usuario jogue par ou impar e progrma pare de ser executado caso o pc GANHE

from random import randint
while True:
    pc = randint(0,11)
    u = int(input('Digite um número: '))
    e = str(input('Você deseja par ou ímpar? ')).lower().strip()
    r = (u + pc)
    if r % 2 == 0:
        x = 'par'
    if r % 2 != 0:
        x = 'ímpar'
    if pc % 2 == 0 and u % 2 == 0 and e == 'ímpar':
        break
    if pc % 2 == 0 and u % 2 != 0 and e == 'par':
        break
    if pc % 2 != 0 and u % 2 == 0 and e == 'par':
        break
    if pc % 2 != 0 and u % 2 != 0 and e == 'ímpar':
        break
    if pc % 2 == 0 and u % 2 == 0 and e == 'par':
        print(f'Parabéns, você selecinou {u} e o pc selecionou {pc}, a somar é {pc + u}, número {x}!')
    if pc % 2 == 0 and u % 2 != 0 and e == 'ímpar':
        print(f'Parabéns, você selecinou {u} e o pc selecionou {pc}, a somar é {pc + u}, número {x}!')
    if pc % 2 != 0 and u % 2 == 0 and e == 'ímpar':
        print(f'Parabéns, você selecinou {u} e o pc selecionou {pc}, a somar é {pc + u}, número {x}!')
    if pc % 2 != 0 and u % 2 != 0 and e == 'par':
        print(f'Parabéns, você selecinou {u} e o pc selecionou {pc}, a somar é {pc + u}, número {x}!')
print(f'PERDEU. Você selecinou {u} e o pc selecionou {pc}, a soma é {u + pc}, número {x}!')