#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.
eleitores = int(input('Digite o número de eleitores: '))
brancos = int(input('Digite o número de votos brancos: '))
nulos = int(input('Digite o número de votos nulos: '))
validos = int(input('Digite o número de votos validos: '))
percenbrancos = (brancos / eleitores) * 100
percennulos = (nulos / eleitores) * 100
percenvalidos = (validos / eleitores) * 100
print(f'Percentual de votos brancos: {percenbrancos}%')
print(f'Percentual de votos nulos: {percennulos}%')
print(f'Percentual de votos validos: {percenvalidos}%')