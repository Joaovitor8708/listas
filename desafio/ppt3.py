jogador1 = input('Digite seu nome: ')
jogador2 = input('Digite seu nome: ')
cont = 0
for x in range(3):
    ppt1 = input(f'{jogador1} pedra, papel ou tesoura? ').upper()
    ppt2 = input(f'{jogador2} pedra, papel ou tesoura? ').upper()
    if ppt1 == ppt2:
        print('Empate, vamos outra rodada.')
        ppt1 = input(f'{jogador1} Escolha: pedra, papel ou tesoura? ').upper()
        ppt2 = input(f'{jogador2} Escolha: pedra, papel ou tesoura? ').upper()
    if ppt1 == 'PEDRA' and ppt2 == 'PAPEL':
        print(f'{jogador2} venceu.')
    elif ppt1 == 'PEDRA' and ppt2 == 'TESOURA':
        print(f'{jogador1} venceu.')
    elif ppt1 == 'TESOURA' and ppt2 =='PEDRA':
        print(f'{jogador2} venceu.')
    elif ppt1 == 'TESOURA' and ppt2 =='PAPEL':
        print(f'{jogador1} venceu.')
    elif ppt1 == 'PAPEL' and ppt2 =='PEDRA':
        print(f'{jogador1} venceu.')
    elif ppt1 == 'PAPEL' and ppt2 =='TESOURA':
        print(f'{jogador2} venceu.')