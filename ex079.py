#usuario digita varios numeros e isso é atribuido a uma lista.
# Caso o numero já exista, ele não será adicionado.
# No final apareça todos os valores digitados em ordem crescente
lista = []
d = 's'
for c in range (0,5):
    n = int(input('Digite um número inteiro: '))
    if n == d:
        lista.remove(n)
    d = n
    lista.append(n)
print(f'{sorted(lista)}')