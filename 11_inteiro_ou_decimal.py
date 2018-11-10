# (Python.org.br) Faça um Programa que peça um número e informe se o número é inteiro ou decimal.

num = float(input('Informe um número: '))

if num % 1 == 0:
    print("Número inteiro")
else:
    print("Número decimal")
