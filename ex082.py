#uma lista com varios numeros
#duas listas extras com os pares e com os impares, cada
#mostre as tres listas.

lista = []
lista_par = []
lista_impar = []

for c in range (0,10):
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
print(f'A lista é: {lista}\n'
      f'A lista par é: {lista_par}\n'
      f'A lista ímpar é: {lista_impar}')