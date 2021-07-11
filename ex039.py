#Faça um programa em que o usuário informe seu ano de nascimento. O programa deve retornar:
# se o jovem já precisa se alistar, quanto tempo falta para ele se alistar ou quanto tempo está atrasado

i = int(input('Olá, em que ano você nasceu? '))
n = 2020 - i
if n < 18:
    print(f'Você ainda não precisa se alistar. Faltam {18 - n} ano(s) ainda.')
elif n == 18:
    print(f'Você deve se alistar esse ano.')
elif n > 18:
    print(f'Caso você ainda não tenha se alistado, você está atrasado em {n - 18} ano(s).')
