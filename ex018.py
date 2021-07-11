#Faça um programa que leia um ângulo qualquer e
#Mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = float(input("Digite o valor do ângulo: "))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print(f'O SENO de {a} é {sen:.2f} \nO COSSENO de {a} é {cos:.2f} \nA TANGENTE de {a} é {tan:.2f}')

