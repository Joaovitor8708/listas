'''Faça um algoritmo que leia 30 valores do
tipo inteiro e armazene-os em um vetor.
A seguir, o algoritmo deverá informar
(1) todos os números pares que existem no
vetor;
(2) o menor e o maior valor existente no
vetor;
(3) quantos dos valores do vetor são
maiores que a média desses valores:'''
vetores = [0] * 3
mai_v = men_v = 0
soma = 0
pares = []
for i in range(30):
    vetores[i] = int(input(f'Digite o {i + 1}º valor: '))
    if i == 0:
        mai_v = men_v = vetores[i]
pares = [k for k in vetores if k % 2 == 0]
for k in vetores:
    if k < men_v:
        men_v = k
    if k > mai_v:
        mai_v = k
    soma += k
media = soma / 30
v_v_a_m = sum(1 for j in vetores if j > media)
print(f'Esse é o seu vetor: {vetores}')
print(f'Estes são os números pares do seu vetor: {pares}')
print(f'Este é o maior valor no seu vetor: {mai_v}')
print(f'Este é o menor valor no seu vetor: {men_v}')
print(f'Esta é a média dos valores do vetor: {media:.1f}.\nSão {v_v_a_m} valores acima da média no vetor.')