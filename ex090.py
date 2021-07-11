#um programa que leia o nome de um aluno e sua média e tambem guarde sua situação em um dicionario.
#No final, mostre esse dic

aluno = str(input('Digite o nome do aluno: '))
media = float(input('Qual a média desse aluno? '))
if media < 7:
    a = 'Recuperação.'
else:
    a = 'APROVADO.'
dic = {'aluno': aluno, 'media': media, 'avaliação': a}
print(dic)
