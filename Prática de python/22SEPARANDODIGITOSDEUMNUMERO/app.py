# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
from time import sleep
n = int(input("DIGITE O NÚMERO: "))
transformaemstr = str(n)
print(f"ANALISANDO O NÚMERO {n}...")
print(f"""UNIDADE: {n[3]}
DEZENA:{n[2]}
CENTENA:{n[1]}
MILHAR: {n[0]}""")

