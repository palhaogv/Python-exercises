#crie um programa onde o usuario digite valores numericos e cadastre-os em uma lista
#ja na posição correta, sem usar sort.
#no final, mostre a lsita ordenada

lista = []
for l in range(0,7):
    n = int(input('Digite um número: '))
    lista.insert(n-7,n)
print(f'{lista}')