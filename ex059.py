# Crie um program que leia dois valores e mostre um menu na tela:
#1 - somar
#2 - multiplicar
#3 - maior
#4 - novos numeros
#5 - sair do programa
#seu programa deverá realizar a ação solicitada em cada caso

d = 'SIM'
while d == 'SIM':
    n1 = float(input('Digite um valor para n1: '))
    n2 = float(input('Digite outro valor para n2: '))
    n = int(input('Você deseja? 1) Somar?; 2) Dividir?; 3)Saber qual é o maior?; 4)Digitar novos números?;'
                  'Ou 5 - sair do programa? '))
    if n == 1:
        print(f'A soma dos dois valores é: {n1 + n2:.2f}')
        d = str(input(('Você deseja continuar? Sim ou Não? '))).upper().strip()
    elif n == 2:
        print(f'A divisão do primeiro número pelo segundo é {n1/n2:.2f}')
        d = str(input(('Você deseja continuar? Sim ou Não? '))).upper().strip()
    elif n == 3:
        if n1 > n2:
            print(f'O maior número entre eles é: {n1:.2f}')
            d = str(input(('Você deseja continuar? Sim ou Não? '))).upper().strip()
        elif n2 > n1:
            print(f'O maior número entre eles é : {n2:.2f}')
            d = str(input(('Você deseja continuar? Sim ou Não? '))).upper().strip()
        elif n1 == n2:
            print(f'Os dois valores são iguais.')
            d = str(input(('Você deseja continuar? Sim ou Não? '))).upper().strip()
    elif n == 4:
        d = 'SIM'
    elif n == 5:
        d = 'NÃO'
print('FIM!')


