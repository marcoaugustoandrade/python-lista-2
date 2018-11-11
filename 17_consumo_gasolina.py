distancia = float(input('Informe a distância percorrida (KM): '))
combustivel = float(input('Informe quantos litros de combustível foram gastos: '))

consumo = distancia / combustivel

if consumo < 8:
    print("Venda o carro")
#elif consumo >= 8 and consumo <= 14:
elif consumo >= 8 and consumo <= 14:
    print("Econômico")
elif consumo > 14:
    print("Super econômico")
