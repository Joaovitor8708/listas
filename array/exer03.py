'''altere o exercício anterior para permitir
achar o nome de um aluno na lista'''
quantidade = int(input("Quantos alunos estão na sala? "))
alunos = [''] * quantidade
for x in range(quantidade):
    alunos[x]= input(f"Digite o nome do aluno {x+1}: ")
for y in range(quantidade):
    print(f"Os alunos na sala são: {alunos[y]} e sua posição é {y}")
pesq = input('Qual aluno deseja encontrar: ')
cont = 0
for z in range(quantidade):
    if pesq == alunos[z]:
        print(f'{alunos[z]} posição {z}')
    elif pesq == alunos[z]:
        cont += 1
    else:
        print('Nome não encontrado')
