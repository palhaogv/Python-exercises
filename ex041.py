#A CBB precisa de um programa que diga a categoria do atleta de acordo com o ano de nascimento.
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# Até 20 anos: senior
# Acima: master

from datetime import datetime, timedelta
from math import floor

d = int(input('Que dia você nasceu? '))
m = int(input('Em qual mês você nasceu? '))
y = int(input('Em qual ano você nasceu? '))
n = datetime(y,m,d).toordinal()
t = datetime.today().toordinal()
i = floor((t - n) / 365)
print(f'Sua idade é {(i)} anos.')

if i <= 9:
    print(f'Você está na categoria MIRIM!')
elif 9 < i <= 14:
    print(f'Você está na categoria INFANTIL!')
elif 14 < i <= 19:
    print(f'Você está na categoria JÚNIOR!')
elif 19 < i <= 20:
    print(f'Você está na categoria SENIOR!')
elif 20 < i:
    print(f'Você está na categoria MASTER!')
