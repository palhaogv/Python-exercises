#Refaça o 51 usando while
#Um programa que leia o PRIMEIRO TERMO e a RAZÃO de um PA.
# No final, mostre os 10 primeiros termos dessa progressão

pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão desa PA: '))
cont = 1
while cont <= 10:
    print(f'{pt} > ', end='')
    pt = pt + r
    cont += 1
