'''Faça um código para ler 5 números e
armazenar em um vetor. Após a leitura
total dos 5 números, o código deve
escrever esses 5 números lidos na ordem
inversa'''
lista = [''] * 5
for x in range(5):
    lista[x] = int(input(f'Digite seu {x + 1 }ª Número: '))
for i in range(4, -1,-1):
    print(lista[i])