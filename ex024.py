#crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"
cidade = input('Digite o nome da sua cidade: ')
minuscula = cidade.lower()
prinome = minuscula.split()
print('santo' in prinome[0])
