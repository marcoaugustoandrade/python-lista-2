lado_a = float(input('Informe o lado A do triângulo: '))
lado_b = float(input('Informe o lado B do triângulo: '))
lado_c = float(input('Informe o lado C do triângulo: '))

if lado_a == lado_b and lado_b == lado_c:
    print("O triângulo é equilatéro")
elif (lado_a == lado_b and lado_a != lado_c) or (lado_b == lado_c and lado_b != lado_a):
    print("O triângulo é isósceles")
elif lado_a != lado_b and lado_a != lado_c and lado_b != lado_c:
    print("O triângulo é escaleno")
