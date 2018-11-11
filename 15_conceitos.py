# Escreva um algoritmo classifique uma nota informada pelo aluno, de 0 a 5, em conceitos, da seguinte forma:
# Conceito A: 5
# Conceito B: 4
# Conceito C: 3
# Conceito D: 2
# Conceito E: 1

nota = int(input('Informe a nota do aluno (1-5): '))

if nota == 5:
    print("Conceito A")
elif nota == 4:
    print("Conceito B")
elif nota == 3:
    print("Conceito C")
elif nota == 2:
    print("Conceito D")
elif nota == 1:
    print("Conceito E")
