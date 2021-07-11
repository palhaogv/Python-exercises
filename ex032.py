#um programa em que o usuário digita o ano e mostra se ele é bissexto
a = int(input('Digite o ano que deseja saber se é bissexto ou não: '))
if a%4 == 0:
    print('Sim, esse ano é BISSEXTO!')
else:
    print('Não, esse ano não é BISSEXTO!')