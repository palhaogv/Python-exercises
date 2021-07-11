def leiadinheiro(a):
    if a not in float:
        print('Você não digitou um número tipo FLOAT, (duas casas decimais após o .). Digite novamente.')
        a = float(input('Qual o valor correto: '))
