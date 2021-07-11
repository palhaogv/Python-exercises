#crie um programa que leia o nome, ano de nascimento e a CTPS.
#Cadastrar esses dados em um dicionario com a idade.
#Caso a CTPS seja != 0 o dicionário deve receber tambem o ano de contratação e o salário.
#Acrescente com quantos anos a pessoa vai ser aposentar.

n = str(input('Digite seu nome: '))
a = int(input('Em que ano você nasceu? '))
i = 2020 - a
ctps = int(input('Qual a sua CTPS? '))
disc = {'nome': n, 'ano': a, 'idade': i, 'CTPS': ctps}
if ctps > 0:
    ac = int(input('Qual o seu ano de contratação? '))
    s = float(input('Qual seu salário? '))
    ap = ac + 35
    disc['ano de contratação'] = ac
    disc['salário'] = s
    disc['ano de aposentadoria'] = ap
print(disc)