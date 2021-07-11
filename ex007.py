#Deselvolva um programa que mostre duas notas de um aluno, calcule e mostre a sua média
p1 = float(input('Qual foi a nota de Pedro na primeira prova? '))
p2 = float(input('Qual foi a nota de Pedro na segunda prova? '))
m = (p1 + p2)/2
print('Pedro teve uma média de {}, caso seja maior que 5, ele está aprovado, caso não, está reprovado.'.format(m))
