#desafio 93 com varios jogadores. FAÇA uma tabela com CÓDIGO, NOME, GOLS e TOTAL DE GOLS
#Disponibilize uma ferramenta com analise individual de cada jogador.

gols_por_partida = []
somar_gols = 0
lista_jogadores = []

while True:
    jogador = str(input('Qual o nome do jogador? '))
    partidas = int(input('Quantas partidas ele jogou? '))
    for c in range(0, partidas):
        gols = int(input(f'Quantos gols o {jogador} fez na {c + 1}ª partida? '))
        gols_por_partida.append(gols)
        somar_gols += gols
    disc_jogador = {'nome': jogador, 'partidas': partidas, 'gols': gols_por_partida[:], 'somatorio dos gols': somar_gols}
    lista_jogadores.append(disc_jogador.copy())
    disc_jogador.clear()
    gols_por_partida.clear()
    somar_gols = 0
    d = str(input('Deseja continuar cadastrando jogadores [S/N]? ')).upper()[0]
    while True:
        if d in 'SN':
            break
        else:
            d = str(input('Cidadão, você digitou errado [S/N]: ')).upper()[0]
    if d == 'N':
        break
print('-='*30)
print(' '*30 + 'RESULTADO')
print('-='*30)
print(f'Nome'+' '*10+'Partidas'+' '*10+'Gols'+' '*20+'Somatório dos gols')
for p in lista_jogadores:
        print(p['nome'], end=' '*(14-len(p['nome'])))
        print(p['partidas'], end=' '*17)
        print(p['gols'], end=' '*(24-len(p['gols'])-(p['partidas']*2)))
        print(p['somatorio dos gols'])
print('-='*30)
print(' '*30 + 'FIM')
print('-='*30)



