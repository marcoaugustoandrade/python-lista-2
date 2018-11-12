saque = int(input('Informe o valor do saque: '))

if saque < 10 or saque > 600:
    print("Valor inválido para saque!")
else:
    notas100 = int(saque / 100)
    notas50 = int((saque - (notas100 * 100)) / 50)
    notas10 = int((saque - (notas100 * 100) - (notas50 * 50)) / 10)
    notas5 = int((saque - (notas100 * 100) - (notas50 * 50) - (notas10 * 10)) / 5)
    notas1 = int(saque - (notas100 * 100) - (notas50 * 50) - (notas10 * 10) - (notas5 * 5))

    print("Notas de 100 %d" % notas100)
    print("Notas de 50 %d" % notas50)
    print("Notas de 10 %d" % notas10)
    print("Notas de 5 %d" % notas5)
    print("Notas de 1 %d" % notas1)
