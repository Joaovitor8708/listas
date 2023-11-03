import time

print('------------------------------------------------------------------------>Bem Vindo ao jogo ANIMAL<------------------------------------------------------------------------')
import random
class Animal:
    def __init__(self,nome):
        self.nome = nome
    def falar(self):
        pass
    def lutar(self, outro_animal):
        vencedor= random.choice([self, outro_animal])
        return f'{vencedor.nome} venceu a briga'
class Cachorro(Animal):
    def falar(self):
        time.sleep(2)
        return 'Au Au Au Au Au, eu vou ganhar Zafi!'
class Gato(Animal):
    def falar(self):
        time.sleep(2)
        return 'Miau Miau Miau, você está muito enganado tobi, haha'

tobi = Cachorro('Tobi')

print('Tobi vai se apresentar!!!!!!!!!!!!!!!!!!!!!!!!!!')
print(tobi.falar())

zafi = Gato('Zafi')
time.sleep(2)
print('Agora é a vez de Zafiiiiiiiii!!!!!')
print(zafi.falar())
time.sleep(2)
print('FAÇAM SUAS APOSTAS!!')
time.sleep(3)
print(tobi.lutar(zafi))