#faça uma função que receba uma msenagem e ela se padronize: ----- 'ola mundo' -----
def mensagem(msg):
    print('-'*10, end='')
    print(msg, end='')
    print('-'*10)


a = str(input('Digite uma mensagem: '))
mensagem(a)