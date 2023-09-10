"""Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500."""


s = 0
p = 0 #são acumaladores
for m3 in range (1,501, 2):  # para ir pulando para os números impas depois de 1
     if m3 % 3 == 0:
       s = s + 1 #contar os quantas vezes foi acionado o if ou quantos números foram encontrados que são multiplos de 3
     p += m3

print(f"foram encontrado {s} números que são  multiplo por 3 e esse é resultado da soma: {p}")