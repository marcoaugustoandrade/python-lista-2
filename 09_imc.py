peso = float(input('Informe o seu peso (KG): '))
altura = float(input('Informe sua altura (cm): '))

imc = peso / (altura / 100 * altura / 100)

if imc <= 18.5:
    print("Abaixo do peso")
elif imc >= 18.6 and imc <= 24.9:
    print("Saudável")
elif imc >= 25 and imc <= 29.9:
    print("Peso em excesso")
elif imc >= 30 and imc <= 34.9:
    print("Obsesidade grau I")
elif imc >= 25 and imc <= 39.9:
    print("Obesidade grau II")
elif imc >= 40:
    print("Obesidade grau III")