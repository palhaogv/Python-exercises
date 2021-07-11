#Valor de um produto considerando seu preço base + forma de pagamento
# 1 - à vista: dinheiro ou cheque = 10% de desconto
# 2 - à vista no cartão: 5% de desconto
# 3 - em até 2x no cartão: preço normal
# 4 - 3x ou mais no cartão: 20% de juros

v = float(input('Qual o valor do produto? '))
fp = int(input('Qual a forma de pagamento? Sendo: \n'
               '1 - à vista (dinheiro ou cheque);\n'
               '2 - à vista no cartão;\n'
               '3 - em até 2x no cartão;\n'
               '4 - 3x ou mais no cartão.\n'
               '\n'
               ''))

if fp == 1:
    print(f'O valor total de sua compra é {v * 0.9}')
elif fp == 2:
    print(f'O valor total de sua compra é {v * 0.95}')
elif fp == 3:
    print(f'O valor total de sua compra é {v}')
elif fp == 4:
    print(f'O valor total de sua compra é {v * 1.2}')
