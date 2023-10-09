'''Altere o sistema anterior e faça um sistema
de login, pedindo a senha do usuário e
mostrando seu nome e a mensagem, login
efetuado com sucesso.'''
lista1 = [''] * 1
lista2 = [''] * 1
for x in range(1):
    lista1[x] = input('Informe seu nome: ')
    lista2[x] = input('Informe sua senha: ')
print('Agora faça o login: ')
senha = input('Digite a sua senha: ')
if senha == lista2[0]:
    print(f'Bem Vindo {lista1[0]}, login efetuado com sucesso. ')
else:
    senha = input('senha incorreta. Digite sua senha novamente: ')
