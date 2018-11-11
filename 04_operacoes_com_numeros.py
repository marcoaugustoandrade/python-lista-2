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

if resultado % 2 == 0:
    par_impar = "par"
else:
    par_impar = "ímpar"

if resultado >= 0:
    positivo_negativo = "positivo"
else:
    positivo_negativo = "negativo"

if resultado % 1 == 0:
    inteiro_decimal = "inteiro"
else:
    inteiro_decimal = "decimal"

print("O resultado da operação é %.2f, %s, %s e %s" % (resultado, par_impar, positivo_negativo, inteiro_decimal))
