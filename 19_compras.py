compra = float(input('Informe o valor total da compra: '))
print("Formas de pagamento: ")
print("a) à vista com desconto de 5%")
print("b) em 3 parcelas sem juros")
print("c) em 5 parcelas com acréscimo de 2%")
print("d) em 10 parcelas com acréscimo de 8%")
pagamento = input('Informe a forma de pagamento escolhida: ')

if pagamento == 'a':
    print("O valor da compra será de R$ %.2f" % (compra * 0.95))
elif pagamento == 'b':
    print("O valor da compra será de R$ %.2f" % compra)
    print("O valor de cada parcela será de R$ %.2f" % (compra / 3))
elif pagamento == 'c':
    print("O valor da compra sera de R$ %.2f" % (compra * 1.02))
    print("O valor de cada parcela será de R$ %.2f" % ((compra * 1.02) / 5))
elif pagamento == 'd':
    print("O valor da compra sera de R$ %.2f" % (compra * 1.08))
    print("O valor de cada parcela será de R$ %.2f" % ((compra * 1.08) / 10))
