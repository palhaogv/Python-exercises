#faça um programa que mostre a tabuada de varios numeros, o programa será interrompido quando
# o usuário digitar um valor negativo.

cont = 0
n = 1
while True:
    t = int(input('Digite o valor da tabuada: '))
    if t < 0:
        break
    cont += 1
    if cont == 1:
        print(f'A tabuada do {t} é: ', end='')
    print(f'{t*1}, {t*2}, {t*3}, {t*4}, {t*5}, {t*6}, {t*7}, {t*8}, {t*9}, {t*10}')
print('Você digitou um valor negativo.')


'''t = int(input('Digite o número que deseja a tabuada: '))
n = 1
cont = 0
while True:
    if cont == 0:
        print(f'A tabuada do {t} é: ', end='')
    cont += 1
    n = t*cont
    print(f'{n} ', end='')
    if cont == 10:
        cont = 0
        n = 1
        c = int(input('\nVocê deseja continuar? Digite 1 para sim e 2 para não: '))
        if c == 1:
            t = int(input('Digite o número que deseja a tabuada: '))
            print(f'A tabuada do {t} é: ', end='')
            cont += 1
            n = t * cont
            print(f'{n} ', end='')
        if c == 2:
            break
print('FIM!')'''




