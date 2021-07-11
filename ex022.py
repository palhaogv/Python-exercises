#Crie um programa que leia o nome completo de uma pessoa e mostre:
#o nome com todas as letras maiúsculas
#o nome com todas minúsculas
#quantas letras ao todo(sem considerar espaços)
#quantas letras tem o primeiro nome

nc = str(input('Qual seu nome completo? '))
print(nc.upper())
print(nc.lower())
se = nc.replace(' ','')
print(len(se))
d = nc.split()
print(len(d[0]))

