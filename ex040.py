#Crie um programa que leia a média de duas provas de um aluno e informe se ele está
#APROVADO: n >= 7
#RECUPERAÇÃO: 5 <= n < 7
#REPROVADO:  n < 5

p1 = float(input('Qual a nota da P1? '))
p2 = float(input('Qual a nota da P2? '))
m = (p1 + p2)/2

if m >= 7:
    print(f'Sua nota foi {m}.\n'
          f'\33[1;32mPARABÉNS\33[m, você foi \33[1;32mAPROVADO\33[m!!!')
elif m < 5:
    print(f'Sua nota foi {m}.\n'
          f'Você foi \33[1;31mREPROVADO\33[m.')
elif 5 <= m < 7:
    print(f'Sua nota foi {m}.\n'
          f'Você está de recuperação.')