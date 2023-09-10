"""Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."""

N1 = int(input("Digite um número: "))
D = 0
for i in range(1,N1 + 1):
     if N1 % i == 0:
         print(f"\033[33m {i} \033[m", end=' ')
         D += 1
     else:
         print(f"\033[31m {i} \033[m", end=" ")

print(f"\nO número {N1} foi divido em {D} vezes ")

if D > 2:
     print("o número não é um primo")
else:
     print("O número é primo!")