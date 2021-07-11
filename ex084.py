#Faça um programa que leia o nome e peso de varias pessoas. Guardando tudo em uma lista
#1 - qts pessoas cadastradas?
#2 - uma lista com as pessoas mais pesadas
#3 - uma com as mais leves

lista = list()
cadastro = list()
pesado = leve = 0
listaleve = list()
listapes = list()
while True:
    n = str(input('Nome do participante: '))
    p = float(input('Peso do participante: '))
    cadastro.append(n)
    cadastro.append(p)
    lista.append(cadastro[:])
    cadastro.clear()
    if pesado == 0:
        pesado = p
    if leve == 0:
        leve = p
    if p >= pesado:
        if p > pesado:
            listapes.clear()
        pesado = p
        listapes.append(n)
        listapes.append(p)
    if p <= leve:
        if p < leve:
            listaleve.clear()
        leve = p
        listaleve.append(n)
        listaleve.append(p)
    r = str(input('Quer parar [S/N]? ')).lower()
    if r == 's':
        break
print(lista)
print(leve,pesado)
print(listapes)
print(listaleve)
