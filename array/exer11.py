'''Faça um código para ler um vetor de 30
números. Após isto, ler mais um número
qualquer, calcular e escrever quantas
vezes esse número aparece no vetor.'''
num = [''] * 30
for i in range(30):
    num[i] = int(input(f'Digite o {i + 1}ª número:  '))
cont = 0
num_aleatorio = int(input('Escolha um número para saber quantas vezes ele apareceu no vetor: '))
for z in num:
    if z == num_aleatorio:
        cont += 1
print(f'O Nº {num_aleatorio} apareceu {cont}x na lista')
