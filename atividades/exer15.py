# Escreva um algoritmo para ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
while n1 == n2:
    print('Os valores ão podem ser iguais')
    n1 = float(input('Digite o primeiro número: '))
    n2 = float(input('Digite o segundo número: '))
if n1 > n2:
    print(f'em ordem crescente: {n1} , {n2}')
else:
    print(f'em ordem crescente:{n2}  {n1}')