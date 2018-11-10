# (Python.org.br) Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar, sendo possível somar, subtrair, dividir ou multiplicar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# par ou ímpar;
# positivo ou negativo;
# inteiro ou decimal.

n1 = float(input('Informe um número: '))
n2 = float(input('Informe outro número: '))

operacao = input('Qual operação deseja realizar (+ - * /)? ')

if operacao == '+':
    resultado = n1 + n2
elif operacao == '-':
    resultado = n1 - n2
elif operacao == '*':
    resultado = n1 * n2
elif operacao == '/':
    resultado = n1 / n2

print("%.2f %s %.2f = %.2f" % (n1, operacao, n2, resultado))

