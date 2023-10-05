#pedra, papel ou tesoura
jogador1 = input('Digite seu nome: ')
jogador2 = input('Digite seu nome: ')
continuar = 'Ss'
while continuar in 'Ss':
    ppt1 = input(f'{jogador1} pedra, papel ou tesoura? ').upper()
    if ppt1 != 'PEDRA' or 'PAPEL' or 'TESOURA':
        ppt1 = input(f'{jogador1} escolha apenas uma dessas opções:\n'
                     f'Pedra, papel ou tesoura? ').upper()
    ppt2 = input(f'{jogador2} pedra, papel ou tesoura? ').upper()
    if ppt2 != 'PEDRA' or 'PAPEL' or 'TESOURA':
        ppt2 = input(f'{jogador2} escolha apenas uma dessas opções:\n'
                     f'Pedra, papel ou tesoura? ').upper()
    while ppt1 == ppt2:
        print('Empate, vamos outra rodada.')
        ppt1 = input(f'{jogador1} Escolha: pedra, papel ou tesoura? ').upper()
        ppt2 = input(f'{jogador2} Escolha: pedra, papel ou tesoura? ').upper()
    if ppt1 == 'PEDRA' and ppt2 == 'TESOURA' or ppt1 == 'TESOURA' and ppt2 == 'PAPEL' or ppt1 == 'PAPEL' and ppt2 == 'PEDRA':
        print(f'{jogador1} VENCEU.')
    else:
        print(f'{jogador2} VENCEU.')
    continuar = input('Deseja continuar? ')