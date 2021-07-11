#crie um lista composta com duas notas de varios alunos. No final, mostre o boletim com a media de todos os alunos
#e que consiga mostrar individualmente o valor de cada aluno procurado

sala = []
aluno =[]
media_ind = 0
media_sala = 0
n = int(input('Quantos alunos tem na sala? '))
for c in range(1, n+1):
    a = str(input(f'Qual o nome do aluno {c}? '))
    n1 = float(input(f'Qual foi a primeira nota do(a) {a}? '))
    n2 = float(input(f'Qual foi a segunda nota do(a) {a}? '))
    media_ind = (n1 + n2)/2
    aluno.append(a)
    aluno.append(n1)
    aluno.append(n2)
    aluno.append(media_ind)
    sala.append(aluno[:])
    aluno.clear()
    media_sala += media_ind
print(f'A sala têm {n} alunos. A média geral da turma foi {media_sala / n}.\n')
print(f'{sala}')

while True:
    d = str(input('Você deseja saber a média de um aluno individualmente [S/N]? ')).lower()
    if d == 's':
        e = int(input('Qual aluno? '))
        print(f'A média do aluno {sala[e][0]} foi: {sala[e][3]}')
    else:
        break