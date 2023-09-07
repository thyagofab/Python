#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("DIGITE SEU NOME COMPLETO: ")).strip().upper()
print(f"SEU NOME TEM SILVA ? {'SILVA' in nome}")