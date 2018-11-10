# Escreva um algoritmo que leia 2 notas de um aluno do IFRO e informe se o mesmo está aprovado ou reprovado na disciplina, considerando que para aprovação a nota tem que ser maior ou igual a 6.

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

if (n1 + n2) / 2 >= 6:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado!")
