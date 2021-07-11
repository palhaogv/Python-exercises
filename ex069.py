#crie um programa que leia o nome, sexo e idade de varias pessoas e pergunte se o usuario quer continuar
# após a parada, deve mostar quantos homens menores do que 18 e quantas mulheres menores do que 20 e quantos
#homens cadastrados

contm18 = 0
contf20 = 0
contm = 0

while True:
    n = str(input('Qual seu nome? '))
    s = str(input('Qual seu sexo? Digite M para masculino ou F, feminino: ')).upper().strip()
    i = int(input('Qual sua idade? '))
    if s == 'M' and i < 18:
        contm18 += 1
    if s == 'F' and i < 20:
        contf20 += 1
    if s == 'M':
        contm += 1
    e = str(input('Deseja continuar? (responda SIM ou NÃO): ')).upper().strip()
    if e == 'NÃO':
        break
print(f'A quantidade de homens cadastrados foi: {contm}.\n'
      f'A quantidade de homens menores de 18 anos foi: {contm18}\n'
      f'A quantidade de mulheres menores de 20 anos foi: {contf20}')