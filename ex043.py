#IMC
#Abaixo de 18.5: abaixo do peso
# Entre 18.5 e 25: peso ideal
# Entre 25 até 30: sobrepeso
# Entre 30 até 40: obesidade
# Acima de 40: obesidade mórbida

print('Quer calcular seu IMC(Indice de massa corporal)?')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
res = peso/(altura*altura)

if res < 18.5:
    print(f'Cuidado, seu IMC é {res:.2f}. Você está abaixo do peso.')
elif 18.5 <= res < 25:
    print(f'Legal, seu IMC é {res:.2f}. Você está no peso ideal.')
elif 25 <= res < 30:
    print(f'Cuidado, seu IMC é {res:.2f}. Você está no sobrepeso.')
elif 30 <= res < 40:
    print(f'Cuidado, seu IMC é {res:.2f}. Você está obeso.')
else:
    print(f'Tome cuidado, seu IMC é {res:.2f} e você está com obesidade mórbida.')