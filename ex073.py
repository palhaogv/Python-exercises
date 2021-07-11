#crie uma tupla com os 20 primeiros colocados da tabela de classificação do brasileirão
#mostre os: 5 premeiros, os últimos 4, a lista em ordem alfabética, em que posição está a chapecoense.

tabela = 'flamengo', 'santos', 'palmeiras', 'gremio', 'at paranaense', 'são paulo', 'inter', 'corinthians', 'goias', 'fortaleza'

print(f'Os primeiros colocados do brasileirão são: {tabela[:4]}')
print(f'Os últimos colocados do brasileirão são: {tabela[6:]}')
print(f'Em ordem alfabética: {sorted(tabela)}')