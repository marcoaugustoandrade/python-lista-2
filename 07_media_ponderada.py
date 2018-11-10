# (BACKES, 2012) Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova tem peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.

p1 = float(input('Informe a nota da prova 1: '))
p2 = float(input('Informe a nota da prova 2: '))
p3 = float(input('Informe a nota da prova 3: '))

nf = ((p1 * 1) + (p2 * 1) + (p3 * 2)) / (1 + 1 + 2)

if nf >= 60:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
