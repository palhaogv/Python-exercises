#Faça o programa que leia o sexo de uma pessoa (valores M e F). Peça a digitação novamente caso esteja errado.

s = 'G'
while s != 'M' and s != 'F':
    s = str(input('Digite M para masculino ou F para feminino: ')).upper().strip()
    if s != 'M' and s != 'F':
        print(f'Você digitou {s} e {s} não é um gênero. Digite ou M ou F.')
print('Obrigado!')
