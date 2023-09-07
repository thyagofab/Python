"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos 
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado."""

dias = int(input("QUANTOS DIAS ALUGADOS? "))
km = float(input("QUANTOS KM RODADOS? "))
print(f"O TOTAL A PAGAR É DE R${(60*dias) + (0.15*km)}")

#forma melhorada

print("-="*30)
print(f"{'LOCADORA':^60}")
print("-="*30)

carro = dict()

carro['MODELO DO CARRO'] = str(input("DIGITE O MODELO DO CARRO: "))
carro['MÊS QUE ALUGOU '] = str(input("DIGITE O MÊS QUE ALUGOU O CARRO: "))
carro['ANO QUE ALUGOU '] = int(input("O ANO QUE ALUGOU O CARRO: "))
carro['DIAS'] = int(input("QUANTOS DIAS QUE PASSOU COM CARRO: "))
carro['KM RODADO'] = int(input("KM RODADOS: "))
carro['TOTAL A PAGAR'] = (60*carro['DIAS']) + (0.15*carro['KM RODADO'])

print("-="*30)
print(print(f"{'RESUMO A PAGAR':^60}"))
print("-="*30)
for k,v in carro.items():
    print(f'{k} = {v}',end='')
    print()
print("-="*30)
