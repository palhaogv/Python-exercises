#Faça um programa que mostre uma contagem regressiva com um segundo entre eles.
from time import sleep
for c in range (10, 0, -1):
    print(c)
    sleep(1)
print('FIM.')