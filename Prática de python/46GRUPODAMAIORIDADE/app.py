"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."""

from datetime import date

maiores = 0
menores = 0

Ano_atual = date.today().year

for tempo in range(1, 8):
     nascimento = int(input(f"digite sua data de nascimento {tempo} pessoa: "))
     idade_maiores_menores = Ano_atual - nascimento
     if idade_maiores_menores >= 18:
         maiores += 1 #se coloca para começar a contar, pois se pessoa for de acordo com a concordancia acrecenta aí +1
     else:
         menores += 1
print(f"Das 7 pessos se encontra {maiores} de maiores e {menores} de menores")
