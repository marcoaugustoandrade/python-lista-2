# (Python.org.br) Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input('Informe um valor: '))

if num > 0:
    print("O número informado é positivo!")
elif num < 0:
    print("O número informado é negativo!")
else:
    print("O número informado é neutro!")
