#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
#quantas partidas jogou. Depois vai ler quantos gols em cada partida. No final isso é um dic com o total de gols

jogador = str(input('Qual o nome do jogador? '))
partidas = int(input('Quantas partidas ele jogou? '))
gols_por_partida = []
somar_gols = 0
for c in range(0, partidas):
    gols = int(input(f'Quantos gols o {jogador} fez na {c + 1}ª partida? '))
    gols_por_partida.append(gols)
    somar_gols += gols
disc_jogagor = {'nome': jogador, 'partidas': partidas, 'gols': gols_por_partida, 'somatorio dos gols': somar_gols}
print(disc_jogagor)