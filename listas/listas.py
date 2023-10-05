'''Perguntar ao usuário quantos alunos tem
na sala e criar um array, unidimensional
(Vetor) com o nome de todos os alunos da
sala'''
quantidade = int(input('Digite quantos alunos tem na sala: '))
alunos = ['']*quantidade

for x in range(quantidade):
    alunos[x] = input('Digite o nome dos alunos: ')
for y in range(quantidade):
    print(alunos[y], y)
