class Pessoa:
    def _init_(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.comendo = False
        self.dormindo = False
        self.falando = False
        self.acordando = False
    def comer(self):
        if self.comendo == True:
            print(f'{self.nome}, já está comendo')
        elif self.falando == True:
            print(f'{self.nome}, não pode falar enquanto come')
        elif self.dormindo == True:
            print('Não pode comer enquanto dorme')
        else:
            print(f'{self.nome}, foi comer.')
            self.comendo = True

    def dormir(self):
        if self.dormindo == True:
            print(f'{self.nome}, ele não pode dormir por que já está dormindo')
        elif self.falando == True:
            print(f'{self.nome}, não pode falar enquanto dorme')
        elif self.comendo == True:
            print(f'{self.nome}, não pode comer enquanto dorme')
        else:
            print(f'{self.nome}, foi dormir.')
            self.dormindo = True

    def falar(self):
        if self.falando == True:
            print(f'{self.nome}, ele não pode falar por que já está falando')
        elif self.dormir == True:
            print(f'{self.nome}, não pode falar enquanto dorme')
        elif self.comendo == True:
            print(f'{self.nome}, não pode falar enquanto come')
        else:
            print(f'{self.nome}, está Falando.')
            self.falando = True
    def acordar(self):
        if self.acordando == True:
            print(f'{self.nome} já está acordado')
        elif self.comendo == True:
            print(f'{self.nome} está comendo')
        elif self.falando == True:
            print(f'{self.nome} está falando')
        elif self.dormindo == True:
            print(f'{self.nome} acordou')
    def apresentar(self):
        print(f'Olá meu nome é {self.nome}, tenho {self.idade} anos e peso {self.peso} Kg')