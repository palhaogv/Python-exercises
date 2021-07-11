#faça uma função contador(). Que receba três parâmetros: inicio, fim, passo.
#Criar de 1 até 10 e 1 em 1.
#de 10 a 0, de 2 em 2
#Contagem personalizada.
from time import sleep

def contador(i, f, p):
    cont = 0
    print('-=' * 20)
    print(f'Contando de {i} até {f} de {p} em {p}.')
    sleep(0.2)

    if p == 0:
        p = 1
    if p < 0:
        p *= -1

    if i > f:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            cont -= p
            sleep(0.3)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            cont += p
            sleep(0.3)
    print('FIM')
    print('-=' * 20)


contador(1, 11, 1)
contador(10, 0, 2)

print('Agora é sua vez!!')
inic = int(input('Escolha o início: '))
fim = int(input('Escolha o fim: '))
pas = int(input('Escolha o passo: '))
contador(inic, fim, pas)
