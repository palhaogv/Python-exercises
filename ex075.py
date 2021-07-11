#um tupla com 4 digitos feitos pelo usuario. O programa deve retornar, quatas x apareceu o n 9,
#em que posição apareceu o primeiro 3
#quantos deles foram pares.

a = (int(input('Digite um valor: '))), \
    (int(input('Digite um valor: '))), \
    (int(input('Digite um valor: '))), \
    (int(input('Digite um valor: '))),

cont = 0
if a[0] % 2 == 0:
        cont += 1
if a[1] % 2 == 0:
        cont += 1
if a[2] % 2 == 0:
        cont += 1
if a[3] % 2 == 0:
        cont += 1
print(f'A quantidade de vezes em que o nº 9 apareceu: {a.count(9)}.\n'
      f'{cont} deles são pares.')
if 3 in a:
    print(f'A posição em que o 3 apareceu foi: {a.index(3)+1}')


