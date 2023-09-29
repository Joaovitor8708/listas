#Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!
num1 = float(input('Digite um número: '))
if num1 > 10:
    print(f'{num1} maior que 10')
elif num1 < 10:
    print(f'{num1} menor que 10')
else:
    print(f'{num1} igual a 10')