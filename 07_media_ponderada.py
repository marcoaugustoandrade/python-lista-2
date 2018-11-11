p1 = float(input('Informe a nota da prova 1: '))
p2 = float(input('Informe a nota da prova 2: '))
p3 = float(input('Informe a nota da prova 3: '))

nf = ((p1 * 1) + (p2 * 1) + (p3 * 2)) / (1 + 1 + 2)

if nf >= 60:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
