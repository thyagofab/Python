"""Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente."""

nome = str(input("DIGITE SEU NOME COMPLETO: "))
dv = nome.split()
print(f"MUITO PRAZER EM TE CONHECER, {nome.upper()}!!!")
print(f"O SEU PRIMEIRO NOME É {dv[0]}")
print(f"O SEU ÚLTIMO NOME É {dv[len(dv) - 1 ]}")
