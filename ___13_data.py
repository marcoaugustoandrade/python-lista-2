# (Python.org.br) Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Informe uma data no formato dd/mm/aaaa: ')

dias31 = [1, 3, 5, 7, 8, 10, 12]
dias30 = [2, 4, 6, 10, 11, 12]




# if int(data[-4:]) in range(1,9999):
#     if int(data[3:5]) in range(1,13):
#         if int(data[3:5]) in dias31:
#             if int(data[:2]) in range(1, 32):
#                 print("Data válida!")
#             else:
#                 print("Data inválida")
#         elif int(data[3:5]) in dias30:
#             if int(data[:2]) in range(1, 31):
#                 print("Data válida!")
#             else:
#                 print("Data inválida")
#         elif int(data[3:5]) == 2 and int(data[:2]) in range(1,28):
#             print("Data válida!")
#         else:
#             print("Data inválida")
# else:
#     print("Data inválida")
