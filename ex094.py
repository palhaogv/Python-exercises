#faça um progrma que leia NOME, SEXO e IDADE de varias pessoas e guarde em dicionarios.
# Todos esses dicionarios em uma lista
#quantas pessoas cadastradas? media de idade?uma lista com todas as mulheres.
# uma lista com pessoas acima da media de idade

lista_pessoas = list()
disc_pessoas = dict()
soma_idade = 0
lista_mulheres = list()

while True:
    disc_pessoas['nome'] = str(input('Nome: '))
    disc_pessoas['idade'] = int(input('Idade: '))
    disc_pessoas['sexo'] = str(input('Sexo (M/F): ')).upper()
    while True:
        if disc_pessoas['sexo'] in 'MF':
            break
        else:
            disc_pessoas['sexo'] = str(input('ERROU. Responda apenas M ou F): ')).upper()
    soma_idade += disc_pessoas['idade']
    lista_pessoas.append(disc_pessoas.copy())
    disc_pessoas.clear()
    d = str(input('Deseja continuar (S/N)? ')).upper()
    while True:
        if d in 'SN':
            break
        else:
            d = str(input('ERROU. Responda apenas S ou N): ')).upper()
    if d in 'N':
        break
media_idade = soma_idade / len(lista_pessoas)
print(lista_pessoas)
for c in lista_pessoas:
    if c['idade'] > media_idade:
        print(f'A pessoa {c["nome"]} tem a idade maior que a média.')
for n in lista_pessoas:
    if n['sexo'] == 'F':
        lista_mulheres.append(n['nome'])

print(f'As mulheres cadastradas são: {lista_mulheres}')
print(f'A quantidade de pessoas cadastras é: {len(lista_pessoas)}')
print(f'A média de idade é: {media_idade}')

