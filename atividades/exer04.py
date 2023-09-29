#Crie um algoritmo que receba 3 números e informe qual o maior entre eles.
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))
if num1 > num2 and num3:
    print(f'O maior número é {num1}')
elif num2 > num3:
    print(f'O maior número é {num2}')
else:
    print(f'O maior número é {num3}')