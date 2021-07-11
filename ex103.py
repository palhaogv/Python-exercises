#faça uma ficha(), que receba o nome de um jogador e quantos gols ele marcou.
#o programa deve mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(a='<sem nome>', b=0):
    print(f'O jogador {a} marcou {b} gol(s).')


n = str(input('Nome do jogador: ')).strip()
g = str(input('Gols marcados: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(b=g)
else:
    ficha(n, g)
