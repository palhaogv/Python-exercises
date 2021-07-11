#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule sua área
# e a quantidade de tinta necessária para pintá-la, sabendo que cada L de tinta pinta 2m²
l = float(input('Qual a largura dessa parede? '))
a = float(input('E a altura dela?'))
m = a * l
r = m/2
print(f'Sua parede tem {m}m², sendo assim, é necessário {r}L de tinta para pintá-la')
