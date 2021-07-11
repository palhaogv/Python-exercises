#crie um programa voto() que vai receber o ano de nascimento de uma pessoa. Retornando se ela tem voto
#NEGADO, OPCIONAL ou OBRIGATÓRIO

def voto(ano_nasc):
    idade = 2020 - ano_nasc
    if idade < 16:
        print(f'Você tem {idade} anos, então você não pode votar.')
    if 16 <= idade < 18 or idade >= 65:
        print(f'Você tem {idade} anos, então seu voto é opcional.')
    if 18 <= idade < 65:
        print(f'Você tem {idade} anos, então seu voto é obrigatório.')

a = int(input('Qual seu ano de nascimento? '))
voto(a)