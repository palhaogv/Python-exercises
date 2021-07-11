from random import choice
import emoji

print(f'Vamos jogar JOKEMPÔ?')
print('-'*40)
lista = ['pedra', 'papel', 'tesoura']
cont = 0
while True:
    u = str(input('Escolha entre pedra, papel ou tesoura: ')).lower().strip()
    pc = choice(lista)
    if u == pc:
        print(emoji.emojize(f'Eita, deu \033[1;7mEMPATE\033[m, o computador também escolheu {pc} :grin:', use_aliases=True))
    elif u == 'papel' and pc == 'tesoura' or u == 'tesoura' and pc == 'pedra' or u == 'pedra' and pc == 'papel':
            print(emoji.emojize(f'\033[1;31mPERDEU\033[m!!! O PC escolheu {pc} :cry:', use_aliases=True))
            break
    elif u == 'papel' and pc == 'pedra' or u == 'tesoura' and pc == 'papel' or u == 'pedra' and pc == 'tesoura':
            print(emoji.emojize(f'\033[1;30;42mGANHOU\033[m!!! O PC escolheu {pc} :punch:', use_aliases=True))
            cont += 1
    else:
        print('Você digitou sua aposta errada. Tente novamente!')
if cont <= 2:
    print(f'Você ganhou apenas \033[1;31m{cont}x\033[m do PC.')
elif 2 < cont <= 4:
    print(f'Você ganhou \033[1;33m{cont}x\033[m do PC.')
elif cont > 4:
    print(f'Você ganhou \033[1;32m{cont}x\033[m do PC. CARALHOOOO!!!')
