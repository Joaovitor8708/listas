import random
palavras = ['BRASIL', 'ARGENTINA', 'URUGUAI', 'CHILE', 'COLOMBIA','VENEZUELA', 'EQUADOR', 'PARAGUAI', 'PERU', 'BOLIVIA','SEGUNDA', 'TERCA', 'QUARTA', 'QUINTA', 'SEXTA', 'SABADO', 'DOMINGO']

palavra = random.choice(palavras)

letras_certas = []
letras_erradas = []
chances = 6
boneco = ["  O", " /|\\", " / \\", " |", " /"," \\"]
while True:
    palavra_secreta = ""
    for letra in palavra:
        if letra in letras_certas:
           palavra_secreta += letra
        else:
            palavra_secreta += "_"

    print("\npalavra: " + palavra_secreta)
    print("Tentativas restantes: " + str(chances))

    for i in range(chances, 7):
        if i > 0:
            print(boneco[i - 1])

    if palavra_secreta == palavra:
        print(f"Parabéns!!! Você ganhou. A palavra era: {palavra}")
        break
    if chances == 0:
        print(f"Que pena!! Infelizmente você perdeu, a palavra era: {palavra}")
        break

    letra = input("Digite uma letra: ").upper()

    if letra in letras_certas or letra in letras_erradas:
        print("Você ja tentou essa letra. ")
        continue

    if letra in palavra:
        letras_certas.append(letra)
    else:
        letras_erradas.append(letra)
        chances -= 1
