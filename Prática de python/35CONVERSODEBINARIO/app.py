"""Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1
para binário, 2 para octal e 3 para hexadecimal."""
print("Escolha uma das opções a baixo")
print("-="*10)
print("1 - Para binário")
print("2 - para octal")
print("3 - para hexadecimal")
print("-="*10)

N = int(input("Digite sua opção: "))

if N == 1 or N == 2 or N == 3:
     N1 = int(input("Digite o número que você deseja converter: "))
if N == 1:
     Conv = bin(N1)[2:]
     print(f"Seu número convertido em binário é igual: {Conv}")
elif N == 2:
     Conv = oct(N1)[2:]
     print(f"Seu número convertido em octal é: {Conv}")
elif N == 3:
     Conv = hex(N1)[2:]
     print(f"Seu número convertido em hexadecimal é: {Conv}")
else:
     print("Não Existe essa opção")   