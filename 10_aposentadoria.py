# Escreva um algoritmo que leia a idade e o sexo de um trabalhador informados pelo usuário e, em seguida, caso o sexo seja feminino e sua idade seja maior ou igual a 60 anos ou sua idade seja maior ou igual a 65 anos, informe que o(a) trabalhador está em condições de se aposentar.

idade = int(input('Informe a idade do trabalhador(a): '))
sexo = input('Informe o sexo (m/f): ')

if sexo == 'f' and idade >= 60 or idade >= 65:
    print("Trabalhador(a) em condições de se aposentar!")
