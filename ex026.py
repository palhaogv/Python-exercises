#faça um programa que leia uma frase pelo teclado e mostre:
#quantas vezes que aparece a letra "A"
#Qual posição ela aparece a primeira vez
#qual posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).lower().strip()
a = frase.count('a')
p = frase.find('a')
u = frase.rfind('a')
print(f'A letra A aparece {a} vezes. A primeira vez que ela aparece é na posição {p+1}, já a última vez'
      f', {u+1}.')

