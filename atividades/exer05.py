#Crie um algoritmo que leia um número e diga se ele é par ou ímpar
num1 = float(input('Digite um número: '))
if num1 % 2 ==0:
    print(f'{num1} É um número par')
else:
    print(f'{num1} É um número ímpar')