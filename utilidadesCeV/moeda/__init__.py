def aumentar(a, b=False):
    """Determina um valor em porcentagem a ser acrescido ao valor informado"""
    p = float(input('Em quantos % você deseja aumentar? '))
    r = (p / 100 + 1) * a
    if b == False:
        print(f'O valor {a}, aumentado em {p}% é {r}\n')
    else:
        print(f'O valor {a}, aumentado em {p}% é ', end='')
        moeda(r)


def diminuir(a, b=False):
    """Determina um valor em porcentagem o valor informado ser reduzido"""
    p = float(input('Em quantos % você deseja diminuir? '))
    r = (1 - p / 100) * a
    if b == False:
        print(f'O valor {a}, diminuido em {p}% é {r}\n')
    else:
        print(f'O valor {a}, diminuido em {p}% é ', end='')
        moeda(r)


def dobro(a, b=False):
    """Dobra o valor informado"""
    r = a * 2
    if b == False:
        print(f'O valor {a} dobrado é {r}')
    else:
        print(f'O valor {a} dobrado é ', end='')
        moeda(r)


def metade(a, b=False):
    """Diminui pela metade o valor informado"""
    r = a / 2
    if b == False:
        print(f'O valor {a} pela metade é {r}')
    else:
        print(f'O valor {a} pela metade é ', end='')
        moeda(r)


def moeda(a):
    """Formata um valor tipo float para moeda brasileira = R$"""
    lista = []
    f = str(a)
    for c in range(0, len(f)):
        d = f[c]
        lista.append(d)
        if f[c] == '.':
            lista.insert(c, ',')
            lista.remove('.')
    print('R$ ', end='')
    for c in range(0, len(lista)):
        print(lista[c], end='')
    print('\n')


def resumo():
    d = int(input('Você deseja saber o que cada função faz? \n'
                  'moeda.aumentar [1]\n'
                  'moeda.diminuir[2]\n'
                  'moeda.dobro[3]\n'
                  'moeda.metade[4]\n'
                  'Não[5]: '))
    if d == 1:
        x = aumentar.__doc__
        print(f'{x}')
    if d == 2:
        x = diminuir.__doc__
        print(f'{x}')
    if d == 3:
        x = dobro.__doc__
        print(f'{x}')
    if d == 4:
        x = metade.__doc__
        print(f'{x}')


