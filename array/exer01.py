'''Perguntar ao usuário quantos alunos tem
na sala e criar um array, unidimensional
(Vetor) com o nome de todos os alunos da
sala'''
quantidade = int(input("Quantos alunos estão na sala? "))
alunos = [''] * quantidade
for x in range(quantidade):
    alunos[x]= input(f"Digite o nome do aluno {x+1}: ")
for y in range(quantidade):
    print(f"Os alunos na sala são: {alunos[y]}")