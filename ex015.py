#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.
d = int(input('Qual a quantidade de dias de utilização do carro? '))
km = int(input('Qual a quantidade de KM rodados? '))
print(f'O valor do aluguel é R$ {d*60+km*0.15:.02f} .')
