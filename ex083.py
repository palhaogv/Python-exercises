#crie um programa onde o usuario digite uma expressão qualquer que use parenteses.
#o programa deve analisar se os parenteses estão abertos e fecados na posição correta
e = str(input('Digite uma expressão matemática: ')).split()
ej = ''.join(e)
if ej.count('(') % 2 == 0 and ej.count(')') % 2 != 0:
    print(f'Essa expressão está errada. Corriga os parênteses.')
else:
    print(f'Essa expressão matemática está com os parênteses corretos.')
