#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez
frase = str(input("DIGITE UMA FRASE: ")).upper()
print(f"A LETRA 'A' APARECE {frase.count('A')} VEZES NA FRASE")
print(f"A PRIMEIRA LETRA 'A' APARECE NA POSIÇÃO {frase.find('A') + 1} ")
print(f"A PRIMEIRA LETRA 'A' APARECE NA POSIÇÃO {frase.rfind('A') + 1} ")