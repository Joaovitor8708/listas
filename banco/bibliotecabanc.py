class Cliente:
    def __init__(self,numero, saldo, nome, tipo, status, limite):
        self.numero = numero
        self.saldo = saldo
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = limite
    def depositar(self,valor):
        if self.status == False:
            print(f'{self.nome} não possui uma conta ativa.')
        if valor > 0:
            print(f'Saldo anterior = {self.saldo:.2f}.')
            self.saldo += valor
            print(f'Seu novo saldo é {self.saldo:.2f}')
        else:
            print('Valor inválido.')
    def sacar(self,valor):
        if self.status == False:
            print(f'{self.nome} não possui uma conta ativa.')
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f'Você sacou {valor:.2f}, seu novo saldo é de {self.saldo:.2f}')
        else:
            print('Saldo insuficiente.')
    def ativarconta(self):
        if self.status == False:
            print(f'{self.nome}, sua conta foi ativada')
            self.status = True
        else:
            print('Sua conta já está ativada')
    def verificarsaldo(self):
        if self.status == False:
            print(f'{self.nome} não possui uma conta ativa.')
        else:
            print(f'Você tem {self.saldo:.2f} reais')