'''Faça um código para ler um valor N qualquer (que
será o tamanho dos vetores). Após, ler dois
vetores A e B (de tamanho N cada um) e depois
armazenar em um terceiro vetor Soma a soma dos
elementos do vetor A com os do vetor B
(respeitando as mesmas posições) e escrever o
vetor Soma.'''
valorn = int(input('Digite um valor qualquer para ser o tamanho da lista: '))
A = [''] * valorn
B = [''] * valorn
for x in range(valorn):
    A[x]= int(input(f'Digite o {x + 1}ª valor para lista "A ": '))
for i in range(valorn):
    B[i] = int(input(f'Digite o {i + 1} valor para lista "B": '))
soma = [''] * valorn
for z in range(valorn):
    soma[z] = A[z] + B[z]
print(f'A soma dos vetores são : {soma}')