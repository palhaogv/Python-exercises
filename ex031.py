# Faça um programa em que o usuário informe a km de distancia da viagem que deseja fazer e o programa cobre
# R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens maiores

n = float(input('Olá, tudo bem com você?'
                ' Você deseja fazer uma viagem com qual distância? '))
if n > 200:
    print(f'Legal, o valor da sua viagem é de R$ {n * 0.45:.2f}!')
else:
    print(f'Legal, o valor da sua viagem é de R$ {n * 0.5:.2f}!')
