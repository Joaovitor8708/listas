#Crie um código que leia um número diferente de zero e diga se este número é positivo ou negativo
num1 = float(input('Digite um número: '))
if num1 > 0:
    print('Positivo')
elif num1 < 0:
    print('Negativo')
else:
    print('Número igual a zero')