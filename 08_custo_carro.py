custo = float(input('Informe o custo de fábrica: R$ '))

if custo <= 12000.00:
    print("O custo para o consumidor será de R$ %.2f" % (custo + (custo * 0.05)))
elif custo >= 12000.00 and custo <= 25000.00:
    print("O custo para o consumidor será de R$ %.2f" % (custo + (custo * 0.1) + (custo * 0.15)))
elif custo > 25000.00:
    print("O custo para o consumidor será de R$ %.2f" % (custo + (custo * 0.15) + (custo * 0.2)))
