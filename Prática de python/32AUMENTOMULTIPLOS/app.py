"""Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
S = float(input("Qual é o salário do funcionário? R$ "))
if S > 1250:
     print(f"Quem ganha R${S} passa a ganhar R${((S * 0.10) + S)}")
else:
     print(f"Quem ganha R${S} passa a ganhar R${((S * 0.15) + S)}")