#crie um programa que leia 5 pesos e informe qual o maior e qual o menor

maior = 0
menor = 0
for p in range (0, 5):
    peso = float(input('Digite seu peso: '))
    if p == 0:
        maior = peso
        menor = peso
    if maior < peso:
        maior = peso
    if menor > peso:
        menor = peso
print(f'O maior peso foi {maior}Kg e o menor peso foi {menor}Kg.')
