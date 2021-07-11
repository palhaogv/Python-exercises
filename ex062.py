#melhore o 61 perguntando se o usuario quer mostrar mais algum termo,
# se ele digitar 0 termos, encerrar o programa

pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão desa PA: '))
cont1 = 1
cont2 = 1
while cont1 <= 10:
    print(f'{pt}', end='')
    print(' > ' if cont1 < 10 else '.', end='')
    pt = pt + r
    cont1 += 1
a = int(input('\nCaso deseje informar outro termo, basta digitá-lo. Caso não, digite 0: '))
if a != 0:
    while cont2 <= 10:
        print(f'{a}', end='')
        print(' > ' if cont2 < 10 else '.', end='')
        a = a + r
        cont2 +=1
else:
    print('Programa encerrado.')