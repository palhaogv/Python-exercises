#crie uma fatorial() que receba dois parâmetros, o número a calcular e o outro chamado SHOW,
# que será um valor lógico (opcional) se será mostrado na tela o processo do cálculo fatorial.

from time import sleep


def fatorial(a, b=False):
    f = 1
    if not b:
        for c in range(a, 0, -1):
            f *= c
        print(f'O fatorial de {a} é {f}.')
    else:
        for c in range(a, 0, -1):
            f *= c
            print(f'{c}', end=' ')
            sleep(0.25)
            if c > 1:
                print('*', end=' ')
                sleep(0.25)
            else:
                print('=', end=' ')
                sleep(0.25)
        print(f'{f}')


f = int(input('Digite o número que deseja calcular o fatorial: '))
d = str(input('Você deseja ver o cálculo [S/N]? ')).upper().strip()
if d == 'S':
    d = True
else:
    d = False
fatorial(f, d)
