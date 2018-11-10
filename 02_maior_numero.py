# (Python.org.br) Faça um programa que peça dois números e imprima o maior deles.

n1 = int(input('Informe o 1º número: '))
n2 = int(input('Informe o 2º número: '))

if n1 > n2:
    print("O maior número é %d" % n1)
elif n1 < n2:
    print("O maior número é %d" % n2)
else:
    print("Os números informados são iguais!")
