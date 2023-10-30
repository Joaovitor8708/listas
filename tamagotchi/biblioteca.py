class Tamagotchi:
    def __init__(self, nome):
        self.nome = nome
        self.comendo = False
        self.dormindo = False
        self.falando = False
        self.acordando = False
        self.felicidade = 50
        self.energia = 100
        self.barriga_cheia = 50

    def comer(self):
        if self.comendo == True:
            print(f'{self.nome} já está comendo')
        elif self.falando == True:
            print(f'{self.nome} não pode falar enquanto come')
        elif self.dormindo == True:
            print('Não pode comer enquanto dorme')
        else:
            self.comendo = True
            self.felicidade += 5
            self.barriga_cheia += 10
            self.energia -= 5
            print(
                f'{self.nome} foi comer e agora tem, {self.felicidade}'
                f' pontos de felicidade e, {self.barriga_cheia} '
                f'pontos de barriga cheia. Sua energia agora é {self.energia}')

    def parar_de_comer(self):
        if self.comendo == True:
            print(f'{self.nome} parou de comer')
            self.comendo = False
        else:
            print(f'{self.nome} não está comendo, portanto não pode parar')


    def dormir(self):
        if self.dormindo == True:
            print(f'{self.nome} não pode dormir por que já está dormindo')
        elif self.falando == True:
            print(f'{self.nome} não pode falar enquanto dorme')
        elif self.comendo == True:
            print(f'{self.nome} não pode comer enquanto dorme')
        else:
            self.dormindo = True
            self.felicidade += 0
            self.barriga_cheia += 10
            self.energia -= 5
            print(
                f'{self.nome} foi dormir e agora tem, {self.felicidade}'
                f' pontos de felicidade e, {self.barriga_cheia} '
                f'pontos de barriga cheia. Sua energia agora é {self.energia}')

    def falar(self):
        if self.falando == True:
            print(f'{self.nome} não pode falar por que já está falando')
        elif self.dormir == True:
            print(f'{self.nome} não pode falar enquanto dorme')
        elif self.comendo == True:
            print(f'{self.nome} não pode comer enquanto fala')
        else:
            self.falando = True
            self.felicidade += 10
            self.barriga_cheia -= 5
            self.energia -= 5
            print(f'{self.nome} está falando e agora tem, {self.felicidade}'
            f' pontos de felicidade e, {self.barriga_cheia} '
            f'pontos de barriga cheia. Sua energia agora é {self.energia}')

    def parar_de_falar(self):
        if self.falando == True:
            print(f'{self.nome} parou de falar')
            self.falando = False
        else:
            print(f'{self.nome} não está falando, portanto não pode parar')

    def acordar(self):
        if self.acordando == True:
            print(f'{self.nome} já está acordado')
        elif self.comendo == True:
            print(f'{self.nome} está comendo')
        elif self.falando == True:
            print(f'{self.nome} está falando')
        elif self.dormindo == True:
            print(f'{self.nome} acordou')

    def checar_estado(self):
        print(
            f'{self.nome} tem {self.energia} pontos de energia, {self.barriga_cheia} pontos de fome e {self.felicidade} pontos de felicidade.')

pet = Tamagotchi(nome='João')

while True:
    acao = input('Digite a ação que deseja executar (comer, parar de comer, dormir, falar, parar de falar, acordar, checar estado): ').lower()
    if acao == 'comer':
        pet.comer()
    elif acao == 'parar de comer':
        pet.parar_de_comer()
    elif acao == 'dormir':
        pet.dormir()
    elif acao == 'falar':
        pet.falar()
    elif acao == 'parar de falar':
        pet.parar_de_falar()
    elif acao == 'acordar':
        pet.acordar()
    elif acao == 'checar estado':
        pet.checar_estado()
    else:
        print('Ação inválida')