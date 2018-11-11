import math

entrada = input('Informe o horário de entrada (hh:mm):')
saida = input('Informe o horário de saída (hh:mm):')

# Transformando os horários de entrada e saída em minutos
entrada_seg = int(entrada[:2]) * 60 + int(entrada[-2:])
saida_seg = int(saida[:2]) * 60 + int(saida[-2:])

# Totalizando o tempo usado no estacionamento, em horas e arredondando para cima
if int(entrada[:2]) < int(saida[:2]):
    total = math.ceil((saida_seg - entrada_seg) / 60)
else:
    # Caso a hora de entrada seja maior significa que a saída foi no dia seguinte
    total = math.ceil(((23 * 60 + 59) - entrada_seg + saida_seg) / 60)

if total <= 2:
    print("O preço a ser pago é R$ %.2f" % (total * 1))
elif 3 <= total <= 4:
    print("O preço a ser pago é R$ %.2f" % (2 + (total - 2) * 1.4))
elif total >= 5:
    print("O preço a ser pago é R$ %.2f" % (2 + 2.8 + (total - 4) * 2))
