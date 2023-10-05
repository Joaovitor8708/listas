#Faça um algoritmo que receba 2 notas e calcule a média aritmética
'''num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
media = (num1 + num2)/2
print(media)'''
jogador_1 = input('Jogador 1 -> Digite seu nome: ')
jogador_2 = input('Jogador 2 -> Digite seu nome: ')
print()
while True:
    escolha_j1 = input(f'{jogador_1} -> Pedra / Papel / Tesoura ? ').upper()
    escolha_j2 = input(f'{jogador_2} -> Pedra / Papel / Tesoura ? ').upper()
    while escolha_j1 == escolha_j2:
        print(f'< {escolha_j1} X {escolha_j2} > TEEEEEMOS UM DJOGO !!! EMPATOOOU, TENTE NOVAMENTE')
        print()
        escolha_j1 = input(f'{jogador_1} -> Pedra / Papel / Tesoura ? ').upper()
        escolha_j2 = input(f'{jogador_2} -> Pedra / Papel / Tesoura ? ').upper()
    if escolha_j1 == 'PEDRA' and escolha_j2 == 'TESOURA':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j1} quebra a {escolha_j2} > TEEEEMOS UM VENCEDOR: {jogador_1} !!!')
    elif escolha_j1 == 'PEDRA' and escolha_j2 == 'PAPEL':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j2} embrulha a {escolha_j1} > TEEEMOS UM VENCEDOR: {jogador_2} !!!')
    elif escolha_j1 == 'TESOURA' and escolha_j2 == 'PEDRA':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j2} quebra a {escolha_j1} > TEEEEMOS UM VENCEDOR: {jogador_2} !!!')
    elif escolha_j1 == 'TESOURA' and escolha_j2 == 'PAPEL':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j1} corta o {escolha_j2} > TEEEMOS UM VENCEDOR: {jogador_1} !!!')
    elif escolha_j1 == 'PAPEL' and escolha_j2 == 'PEDRA':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j1} embrulha a {escolha_j2} > TEEEMOS UM VENCEDOR: {jogador_1} !!!')
    elif escolha_j1 == 'PAPEL' and escolha_j2 == 'TESOURA':
        print(f'< {escolha_j1} X {escolha_j2} >  < {escolha_j2} corta o {escolha_j1} > TEEEMOS UM VENCEDOR: {jogador_2} !!!')
    print()
    continuar = input('Você deseja continuar jogando ? [S] para "SIM" ou [N] para "NÃO"--> ')
    print()
    if continuar in 'Nn':
        break
print('Programa Encerrado com sucesso! Até a próxima.')