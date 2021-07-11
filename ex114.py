#Acesse o site pudim.com e informe se ele está valido ou não

from requests import get
try:
    x = get('http://pudim.com.br')
    print(x.status_code)
except:
    print('\033[1;31mO site não está acessível no momento. '
          'Verifique sua conexão de internet ou se o site realmente está em uso.\033[m')
else:
    if x.status_code == 200:
        print('\033[1;32mO site está acessível\033[m')