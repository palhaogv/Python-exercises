#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
n = float(input('Digite um número quebrado: '))
import math
print('A porção inteira desse número é {}'.format(math.floor(n)))
