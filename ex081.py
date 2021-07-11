# crie um programa que liste varios numeros e:
#quantos numeros foram digitados?
#a lista em forma decrescente
#se o valor 5 foi digitado

cont = 0
lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    cont += 1
    d = str(input('Deseja continuar? ')).lower().strip()
    if d == 'não':
        break
print(f'A lista digitada em forma decrescente é {sorted(lista)[::-1]}')
print(f'Nessa lista, existem {cont} valores digitados.')
if 5 in lista:
    print('Nessa lista o número 5 está presente.')
