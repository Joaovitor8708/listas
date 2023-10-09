'''altere o exercício anterior e mostre na tela,
ao final, o nome de cada aluno e sua
respectiva posição no array'''
quantidade = int(input("Quantos alunos estão na sala? "))
alunos = [''] * quantidade
for x in range(quantidade):
    alunos[x]= input(f"Digite o nome do aluno {x+1}: ")
for y in range(quantidade):
    print(f"Os alunos na sala são: {alunos[y]} e sua posição é {y}")
