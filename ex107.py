# Criar um moeda.py que tenha aumentar(), diminuir(), dobro() e metade() - FEITO
# Faça um programa que importe esses módulos e use essas funções - FEITO
# moeda() formatado para mostrar o número de forma monetária (ex 108) - FEITO
# as funções devem aceitar um parametro informando se o valor será ou não formatado para a função moeda() (ex109) - FEITO
# crie uma função resumo() que mostre informações sobre as funções criadas no moeda.py(ex110) - FEITO

from utilidadesCeV import moeda, dado

valor = float(input('Digite o valor do produto: R$ '))
real = str(input('Você deseja que esse valor seja apresentado em R$? [S/N] ')).upper().strip()
if real == 'S':
    moeda.aumentar(valor, True)
    moeda.diminuir(valor, True)
    moeda.dobro(valor, True)
    moeda.metade(valor, True)
else:
    moeda.aumentar(valor, False)
    moeda.diminuir(valor, False)
    moeda.dobro(valor, False)
    moeda.metade(valor, False)

moeda.resumo()




