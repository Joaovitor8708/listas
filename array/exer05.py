'''Exercício 05
Ler um vetor A de 10 números. logo em
seguida, ler mais um número e guardar em
uma variável X.
Armazenar em um vetor M o resultado de
cada elemento de A multiplicado pelo
valor X. Logo após, imprimir o vetor M.'''
vetor1 = [''] * 10
for x in range(10):
    vetor1[x] = int(input(f'Digite o {x + 1}ª Número: '))
vetor2 = int(input('Digite o valor para multiplicar cada elemento da lista: '))
vetor3 = [''] * 10
for i in range(10):
    vetor3[i] = vetor1[i] * vetor2
print(f'Os valores da lista: {vetor1}')
print(f'Multiplicador: {vetor2}')
print(f'Lista multiplicada: {vetor3}')