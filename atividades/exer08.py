#Faça um código que receba 4 números e realize a soma deles e a média entre eles. e mostre os resultados.
contador = 0
for x in range(4):
    num = float(input('Digite os número: '))
    contador += num
media = contador / 4
print(media)