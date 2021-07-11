# faça um simulador de caixa eletroinico que pergunte ao usuario quanto ele deseja sacar (n int)
# e o programa deverá informar quantas cédulas serão entregues.
# Considere que o caixa tenha cédulas de R$ 50, R$20, R$10 e R$ 1

cont50 = 0
cont20 = 0
cont10 = 0
cont01 = 0

valor = int(input('Quanto você deseja sacar? '))
if valor // 50 >= 1:
    cont50 = valor // 50
if valor % 50 >= 20:
    cont20 = valor % 50 // 20
if (valor % 50) % 20 >= 10:
    cont10 = ((valor % 50) % 20) // 10
if ((valor % 50) % 20) % 10 >= 1:
    cont01 = (((valor % 50) % 20) % 10) // 1
print(f'Você receberá: \n'
      f'{cont50} notas de R$ 50,00\n'
      f'{cont20} notas de R$ 20,00\n'
      f'{cont10} notas de R$ 10,00\n'
      f'{cont01} notas de R$ 1,00')