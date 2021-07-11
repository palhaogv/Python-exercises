#crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome
nome = input('Digite seu nome completo: ')
minuscula = nome.lower()
silva = 'silva' in minuscula
print(f'A afirmação "você tem Silva no nome" é {silva}')

