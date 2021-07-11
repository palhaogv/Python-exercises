#crie uma matriz 3x3 e preencha com valores lidos pelo teclado
#No final, mostre a matriz na tela com o valor correto.

lista = []

for c in range(1, 10):
    n = int(input(f'Digite o valor da {c}ª posição: '))
    lista.append(n)
print(f'[{lista[0]}][{lista[1]}][{lista[2]}]\n'
      f'[{lista[3]}][{lista[4]}][{lista[5]}]\n'
      f'[{lista[6]}][{lista[7]}][{lista[8]}]\n')