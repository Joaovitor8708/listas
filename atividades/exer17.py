#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se foremcompradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule eescreva o custo total da compra.
macas = int(input('Quantas maças vão ser: '))
if macas < 12:
    preco = 1.30
else:
    preco = 1.0
total = macas * preco
print(f'O preço da(s) maça(s) é: {total}')