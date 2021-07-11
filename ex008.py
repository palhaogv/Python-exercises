#Escreva um programa que leia um valor em m e exiba a conversão em cm e ml
n = float(input('Digite um valor: '))
cm = float(n*100)
ml: float = n*1000
print(f'Esse valor é equivalente à {cm:.2f}cm e a {ml:.2f}ml')
