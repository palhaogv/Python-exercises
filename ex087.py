#soma dos valores pares
#a soma da terceira coluna
#o maior valor da segunda linha

lista = []
somapar = 0
somar3coluna = 0
maiorvalor2 = 0

for c in range(1, 10):
    n = int(input(f'Digite o valor da {c}ª posição: '))
    lista.append(n)
    if n % 2 == 0:
        somapar += n
    if c == 3 or c == 6 or c == 9:
        somar3coluna += n
    if c == 2:
        maiorvalor2 = n
    if (c == 5 or c == 8) and maiorvalor2 < n:
        maiorvalor2 = n
print(f'[{lista[0]}][{lista[1]}][{lista[2]}]\n'
      f'[{lista[3]}][{lista[4]}][{lista[5]}]\n'
      f'[{lista[6]}][{lista[7]}][{lista[8]}]\n')
print(f'A soma dos valores pares é: {somapar}.\n'
      f'A soma da terceira coluna é: {somar3coluna}.\n'
      f'O maior valor da segunda coluna é: {maiorvalor2}.')
