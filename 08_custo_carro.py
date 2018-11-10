# BACKES, 2012) O custo ao consumidor de um carro novo e a soma do custo de fábrica, da comissão do distribuidor, e dos impostos. A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de fábrica e escreva o custo ao consumidor.
#  Custo de fábrica                     % do distribuidor       % dos impostos
#  Até R$ 12.000,00                     5                       isento
#  Entre R$ 12.000,00 e R$ 25.000,00    10                      15
#  Acima de R$ 25.000,00                15                      20

custo = float(input('Informe o custo de fábrica: R$ '))

if custo <= 12000.00:
    print("O custo para o consumidor será de R$ %.2f" % (custo + (custo * 0.05)))
elif custo >= 12000.00 and custo <= 25000.00:
    print("O custo para o consumidor será de R$ %.2f" % (custo + (custo * 0.1) + (custo * 0.15)))
elif custo > 25000.00:
    print("O custo para o consumidor será de R$ %.2f" % (custo + (custo * 0.15) + (custo * 0.2)))
