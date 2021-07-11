#Criar um programa de jokempo, já criado HEHE

from random import choice
import emoji

print('Vamos jogar JOKEMPO?')
u = str(input('Escolha entre pedra, papel ou tesoura: ')).lower().strip()
lista = ['pedra', 'papel', 'tesoura']
pc = choice(lista)
if u == pc:
    print(emoji.emojize(f'Eita, deu \033[1;7mEMPATE\033[m, o computador também escolheu {pc} :grin:', use_aliases=True))
elif u == 'papel' and pc == 'tesoura' or u == 'tesoura' and pc == 'pedra' or u == 'pedra' and pc == 'papel':
        print(emoji.emojize(f'\033[1;31mPERDEU\033[m!!! O PC escolheu {pc} :cry:', use_aliases=True))
elif u == 'papel' and pc == 'pedra' or u == 'tesoura' and pc == 'papel' or u == 'pedra' and pc == 'tesoura':
        print(emoji.emojize(f'\033[1;30;42mGANHOU\033[m!!! O PC escolheu {pc} :punch:', use_aliases=True))
else:
    print('Você digitou sua aposta errada. Tente novamente!')