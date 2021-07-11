#Crie um algoritimo que leia um número e mostre seu dobro, triplo e raíz
n = float(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro de {} é {}, seu triplo é {}, já sua raíz quadrada, {:.2f}'.format(n,d,t,r))
