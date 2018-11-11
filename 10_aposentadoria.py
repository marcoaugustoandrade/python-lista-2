idade = int(input('Informe a idade do trabalhador(a): '))
sexo = input('Informe o sexo (m/f): ')

if sexo == 'f' and idade >= 60 or idade >= 65:
    print("Trabalhador(a) em condições de se aposentar!")
