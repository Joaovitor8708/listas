# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.
idade = int(input('Digite sua idade: '))
mes = int(input('Digite o mês que nasceu: '))
dias = int(input('Digite o dia que nasceu: '))
diasvivos = idade *365 + mes * 30 + dias
print(f'Você viveu {diasvivos} dias')