#crie um programa que leia o nome do produto e seu valor e pergunte se o usuario irá continuar comprando
# ao final, mostre o valor da compra total e quantos itens são superiores a 1000 reais e qual o nome
#do produto mais barato

contp_1000 = 0
valor_comp = 0
cheapper_prod = 0
vcheapper_prod = 0
cont = 0
while True:
    prod = str(input('Digite o nome do produto: '))
    v = float(input('Digite o valor do produto: '))
    valor_comp += v
    if cont == 0:
        cheapper_prod = prod
        vcheapper_prod = v
    if v > 1000.00:
        contp_1000 += 1
    if v < vcheapper_prod:
        cheapper_prod = prod
        vcheapper_prod = v
    cont += 1
    c = str(input('Você deseja continuar? Sim ou Não? ')).upper().strip()
    if c == 'NÃO':
        break
print(f'O valor total de sua compra foi de {valor_comp}, {contp_1000} produto(s) tem valor superior a R$ 1.000,00.\n'
      f'O produtor mais barato é o/a {cheapper_prod}, que custou {vcheapper_prod} reais.')