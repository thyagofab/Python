"""Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite"""

velocidade = float(input("DIGITE A VELOCIDADE DO SEU CARRO EM KM/H: "))
if velocidade >= 80:
    print(f"VOCê FOI MULTADO!! E A MULTA É DE R$ {(velocidade - 80)*7} ")
else:
    print("TENHA UM BOM DIA! DIRIJA COM SEGURANÇA")