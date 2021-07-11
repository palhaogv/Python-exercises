#Um programa que leia o PRIMEIRO TERMO e a RAZÃO de um PA.
# No final, mostre os 10 primeiros termos dessa progressão
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão desa PA: '))
for c in range (pt, r*10+1, r):
    print(c)
