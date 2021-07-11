#um programa que identifique a velocidade de um carro, caso ultrapasse 80km
# o usuário será multado em R$7 por km a mais

from random import randint
n = randint(0,200)
print(f'O carro que acabou de passar está a uma velocidade de {n}km/h.')
if n> 80:
    print(f'Logo, deverá pagar um multa de R$ {float(7.5*(n-80)):.2f}!')
else:
    print(f'Logo, ele está dentro da velocidade correta!')