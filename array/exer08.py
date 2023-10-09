'''Faça um código para ler 5 nomes de
usuários e suas respectivas senhas, e
armazenar cada lista em um array
diferente, após completar a digitação,
imprimir , nome, senha e posição dos
dados no array'''
lista1 = [''] * 5
lista2 = [''] * 5
for x in range(5):
    lista1[x] = input('Informe seu nome: ')
    lista2[x] = input('Informe sua senha: ')
for i in range(5):
    print(f'Nome: {lista1[i]}')
    print(f'Senha: {lista2[i]}')
    print(f'Sua posição: {i}')