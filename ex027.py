#faça um programa que leia o nome completo de uma pessoa.
# mostrando em seguida o primeiro e o último nome separdamente
nome = str(input('Digite seu nome completo: ')).strip()
p = nome.split()
print(f'O seu primeiro nome é {p[0]}. Já seu último nome é {p[len(p)-1]}.')
